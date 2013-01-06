# generate.py -- assemble the pieces
import os
import shutil
import time
from docutils.core import publish_parts

def test():
    s = Scanner(".")
    s.scan_templates()
    s.scan_content()
    s.init_components()
    s.data.build()

# strip extraneous lists
def flatten_list(l):
    if type(l) != list:
        return str(l)
    if len(l) < 1:
        return ""
    elif len(l) == 1:
        return flatten_list(l[0])
    else:
        return map(flatten_list, l)

class SiteData(object):
    def __init__(self):
        self.content = {}
        self.templates = {}
        self.components = {}
        self.output_dir = "output"
    def ensure_dir(self, f):
        d = os.path.dirname(f)
        if not os.path.exists(d):
            os.makedirs(d)
    def render_template(self, tmpl_name, fields):
        print("[SiteData] render_template - {}".format(tmpl_name))
        t = self.templates[tmpl_name]
        repl = {}
        for r in t.replacements:
            if r in t.require:
                print("[render_template] render req'd component: {}".format(t.require[r]))
                repl[r] = self.components[t.require[r]].render(tmpl_name=tmpl_name, fields=fields)
            elif r in fields:                 # allow fields to override components
                repl[r] = fields[r]
            elif r in t.include:
                print("[render_template] render include'd component: {}".format(t.include[r]))
                repl[r] = self.components[t.include[r]].render(tmpl_name=tmpl_name, fields=fields)
            else:
                repl[r] = ""
        for p in t.parent:  # process parent template
            p_tmpl = p[0]
            p_field = p[1]
            # move forward template data, child data, component evaluation
            p_repl = t.metadata.copy()
            p_repl.update(fields)
            p_repl.update(repl)
            p_repl[p_field] = t.content.format(**repl)
            return self.render_template(p_tmpl, p_repl)
        return t.content.format(**repl)
    def write_file(self, filepath, content):
        print("[SiteData] Writing output to {}".format(filepath))
        self.ensure_dir(filepath)
        with open(filepath, 'w') as f:
            f.write(content)
    def build(self):
        output_dir = "output"
        # build out templates
        for name,t in self.templates.iteritems():
            if t.generate:
                for g in t.generate:
                    content_type = g[0]
                    field = g[1]
                    for c in self.content[content_type]:
                        #fields = self.flatten_metadata(c.metadata)
                        fields = c.metadata.copy()
                        fields[field] = c.render()
                        raw_output = self.render_template(name, fields)
                        filepath = os.path.join(output_dir, content_type, c.name) + ".html"
                        self.write_file(filepath, raw_output)
            else:
                fname = name.split('.')[0] + ".html"
                filepath = os.path.join(output_dir, fname)
                self.write_file(filepath, self.render_template(name, {}))

class Scanner(object):
    TEMPLATE_DIR = "template"
    OUTPUT_DIR = "output"
    def __init__(self, base_dir):
        self.data = SiteData()
        self.base_dir = base_dir
        self.generate = []
        self.components = []
    def _scan(self, scan_dir):
        """Scan a folder and collect metadata
            returns a dict keyed by filename
        """
        output = {}
        root = os.path.join(self.base_dir, scan_dir)
        for filename in os.listdir(root):
            # read the metadata
            if filename.startswith('.'):
                continue
            path = os.path.join(root,filename)
            file_info = {}
            file_info['name'] = filename
            file_info['path'] = path
            file_info['metadata'] = {}
            file_info['content'] = ""
            metadata = []
            with open(path,'r') as f:
                line = f.readline()
                while line:
                    if line.startswith(":"):
                        metadata.append(line.strip())
                    else:
                        file_info['content'] += line
                    line = f.readline()
            # pick out the metadata directives
            for md in metadata:
                mds = md.split(' ')
                mds[0] = mds[0].strip(':')
                if mds[0] == 'generate':
                    self.generate.append((mds[1],mds[2],filename))
                if mds[0] == 'require' or mds[0] == 'include':
                    self.components.append(mds[1])
                if mds[0] not in file_info['metadata']:
                    file_info['metadata'][mds[0]] = []
                file_info['metadata'][mds[0]].append(mds[1:])
            output[filename] = file_info
        return output
    def scan_templates(self):
        raw_output = self._scan(Scanner.TEMPLATE_DIR)
        for name,t in raw_output.iteritems():
            self.data.templates[name] = Template(name, t['path'], t['metadata'], t['content'])
    def scan_content(self):
        for gen in self.generate:
            raw_output = self._scan(gen[0])
            self.data.content[gen[0]] = []
            for name,p in raw_output.iteritems():
                self.data.content[gen[0]].append(Content(name, gen[0], p['metadata'], p['content']))
    def init_components(self):
        package = "components"
        for comp in self.components:
            if comp not in self.data.components:
                cls = comp.capitalize()
                imported = getattr(__import__("components." + comp, fromlist=[cls]), cls)
                self.data.components[comp] = imported(self.data)

class Template(object):
    """the template class stores dependencies for rendering a template"""

    import re
    repl_re = re.compile("\{([a-z_-]+)\}")

    def __init__(self, name, path, metadata, content):
        self.parent = []
        self.generate = []
        self.require = {}       # field => component
        self.include = {}       # field => component
        self.replacements = []
        self.name = name
        self.path = path
        self.metadata = metadata
        self.content = content

        # pick apart metadata
        self._build_metadata()
        self._build_replacements()
    def __repr__(self):
        return "Template({}, parent={}, generate={}, require={}, include={})".format(self.name, self.parent, self.generate, self.require, self.include)
    def _build_metadata(self):
        for key,value in self.metadata.iteritems():
            if key == 'provide':
                self.parent = value
            elif key == 'require':
                for comp,field in value:
                    self.require[field] = comp
            elif key == 'include':
                for comp,field in value:
                    self.include[field] = comp
            elif key == 'generate':
                self.generate = value
            else:
                self.metadata[key] = flatten_list(value)
                if type(self.metadata[key]) == list:
                    self.metadata[key] = " ".join(self.metadata[key])
    def _build_replacements(self):
        self.replacements = Template.repl_re.findall(self.content)
class Content(object):
    """the template class stores dependencies for rendering a template"""
    def __init__(self, name, ctype, metadata, content):
        name,ext = name.split('.')
        self.name = name
        self.ext = ext      # the original file extension
        self.ctype = ctype  # the content type (i.e. folder it's in)
        self.metadata = metadata
        self.content = content
        self._build_metadata()

    def _build_metadata(self):
        # this is to allow easy sorting/archiving
        if "published" in self.metadata:
            self.published = self.metadata['published'][-1][0]
            self.metadata["published"] = self.date_parse(self.published)
        else:
            self.published = 0
        if "modified" in self.metadata:
            self.modified = self.metadata['modified'][-1][0]
        else:
            self.modified = self.published
        self.metadata["modified"] = self.date_parse(self.modified)

        for key,value in self.metadata.iteritems():
            self.metadata[key] = flatten_list(value)
            if type(self.metadata[key]) == list:
                self.metadata[key] = " ".join(self.metadata[key])
        if "slug" not in self.metadata:
            self.metadata["slug"] = self.slugify(self.name)
        self.name = self.metadata["slug"]
    def slugify(self, name):                                                                      
        slug = []
        a = ord('a')
        z = ord('z')
        last_chr = True      # true if the last character printed
        for ch in name.lower():
            if ord(ch) >= a and ord(ch) <= z:
                last_chr = True
                slug.append(ch) 
            elif last_chr:
                last_chr = False
                slug.append("-")
        return "".join(slug)
    def __repr__(self):
        return "Content({})".format(self.name)
    def date_parse(self,value):
        try:
            value = float(value)
            return time.strftime("%Y-%m-%d %H%M",time.localtime(float(value)))
        except ValueError:
            return value
    def render(self):
        if self.ext == "rst":
            return publish_parts(self.content, writer_name='html')['body']
        else:
            return self.content

if __name__ == '__main__':
    test()
