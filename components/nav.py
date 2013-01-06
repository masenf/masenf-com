from components import Component
from components.posts import Posts
import time
import os

# set up blog archives
class Archive(Posts):
    def get_content(self):
        return self.content
class Nav(Component):
    def generate_archive(self, ym, content):
        a = Archive(self.data)
        a.content = sorted(content,key=lambda c: c.published,reverse=True)
        fields = {}
        fields['posts'] = a.render()
        fields['nav'] = self.render(ym)
        fields['title'] = "blog > {}".format(ym)
        output = self.data.render_template("blog.tmpl.html", fields)
        relpath = os.path.join("blog","archive",ym + ".html")
        filepath = os.path.join(self.data.output_dir, relpath)
        self.data.write_file(filepath, output)
        return relpath
    def render(self, active=None, tmpl_name=None, fields=None):
        if fields is not None:
            print("[Nav] tmpl_name={}, fields={}".format(tmpl_name, fields.keys()))
        if not hasattr(self, "order"):
            self.archive_months = {}
            for c in self.data.content['blog']:
                ym = time.strftime("%Y-%m",time.localtime(float(c.published)))
                if not ym in self.archive_months:
                    self.archive_months[ym] = []
                self.archive_months[ym].append(c)
            self.order = sorted(self.archive_months.keys(), reverse=True)
            for ym in self.order:
                self.generate_archive(ym, self.archive_months[ym])
        if active is None:
            act = " class='active'"
        else:
            act = ""
        rendered = "<li{}><a href=\"/blog.html\">latest posts</a></li>\n".format(act)
        rendered += "<li class=\"nav-header\">archives</li>\n"
        for ym in self.order:
            if ym == active:
                act = " class='active'"
            else:
                act = ""
            relpath = os.path.join("blog","archive",ym + ".html")
            rendered += "<li{}><a href=\"/{}\">{} ({})</a></li>\n".format(act, relpath, ym, len(self.archive_months[ym]))
        return rendered
