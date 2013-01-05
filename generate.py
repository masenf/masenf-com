# generate.py -- assemble the pieces
import os
from docutils.core import publish_parts


class SiteData(object):
    def __init__(self):
        self.content = {}
        self.templates = {}
        self.components = {}
    def render_template(self, tmpl_name, fields):
        t = self.templates[tmpl_name]
        repl = {}
        for r in t.replacements:
            if r in t.components:
                repl[r] = self.components[r].render()
            elif r in fields:
                repl[r] = fields[r]
            else:
                repl[r] = ""
        return t.content.format(**repl)

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
            with open(path,'r') as f:
                content = f.read()
            file_info = {}
            file_info['content'] = content
            file_info['name'] = filename
            file_info['path'] = path
            file_info['metadata'] = {}
            # pick out the metadata directives
            metadata = filter(lambda x: x.startswith(":"), content.split("\n"))
            for md in metadata:
                mds = md.split(' ')
                mds[0] = mds[0].strip(':')
                if mds[0] == 'generate':
                    self.generate.append((mds[1],mds[2],filename))
                if mds[0] == 'require':
                    self.components.append(mds[1])
                if mds[0] not in file_info['metadata']:
                    file_info['metadata'][mds[0]] = []
                file_info['metadata'][mds[0]].append(" ".join(mds[1:]))
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
                self.data.content[gen[0]].append(Content(name, p['metadata'], p['content']))
    def init_components(self):
        for comp in self.components:
            imported = getattr(__import__("components", fromlist=[comp]), comp)
            self.data.components[name] = imported(self.data)
class Template(object):
    """the template class stores dependencies for rendering a template"""

    import re
    repl_re = re.compile("\{([a-z]+)\}")

    def __init__(self, name, path, metadata, content):
        self.parent = []
        self.generate = []
        self.components = []
        self.replacements = []
        self.name = name
        self.path = path
        self.metadata = metadata
        self.content = content

        # pick apart metadata
        self._build_metadata()
        self._build_replacements()
    def __repr__(self):
        return "Template({}, parent={}, generate={}, components={})".format(self.name, self.parent, self.generate, self.components)
    def _build_metadata(self):
        for key,value in self.metadata.iteritems():
            if key == 'provide':
                for p in value:
                    self.parent.append(p.split(" "))
            elif key == 'require':
                self.components = value
            elif key == 'generate':
                for g in value:
                    self.generate.append(g.split(" "))
    def _build_replacements(self):
        self.replacements = Template.repl_re.findall(self.content)
class Content(object):
    """the template class stores dependencies for rendering a template"""
    def __init__(self, name, metadata, content):
        self.name = name
        self.metadata = metadata
        self.content = content
    def __repr__(self):
        return "Content({})".format(self.name)
