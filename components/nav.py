from components import Component
from components.posts import Posts
import time
import os,sys

# set up blog archives
class Archive(Posts):
    def get_content(self):
        return self.content
class Nav(Component):
    def generate_archive(self, ym, content):
        self.log("Nav", "Generate archive listing for {} ({})".format(ym, len(content)), self.data.level)
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
    def similar_posts(self, slug, tag):
        # get all tags from active_tag database
        atags = self.data.components['active_tags'].tags
        out = "<li class=\"nav-header\">Related Posts</li>\n"
        similars = { }
        simcounts = { }
        tags = tag.split(" ")
        for tag in tags:
            if tag in atags:
                for c in atags[tag]:
                    if c.name != slug:
                        if c.name not in similars:
                            similars[c.name] = c
                            simcounts[c.name] = 0
                        simcounts[c.name] += 1
        ranking = list(simcounts.items())
        ranking.sort(key=lambda x: x[1], reverse=True)
        for similarslug in ranking[0:5]:
            md = similars[similarslug[0]].metadata
            out += "<li><a href=\"{}\">{}</a></li>\n".format(md['link'],md['title'])
        if similars:
            return out
        else:
            return ""       # if there are no other posts, show nothing
    def render(self, active=None, tmpl_name=None, fields=None):
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
        if fields is not None and "tag" in fields:
            rendered += self.similar_posts(fields['slug'], fields['tag'])
        rendered += "<li class=\"nav-header\">archives</li>\n"
        for ym in self.order:
            if ym == active:
                act = " class='active'"
            else:
                act = ""
            relpath = os.path.join("blog","archive",ym + ".html")
            rendered += "<li{}><a href=\"/{}\">{} ({})</a></li>\n".format(act, relpath, ym, len(self.archive_months[ym]))
        return rendered
