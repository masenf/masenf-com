from components import Component
from components.posts import Posts
import os

class Tag_page(Posts):
    def get_content(self):
        return self.content
class Active_tags(Component):
    # create tag pages and turn plain tag lists into
    # links
    def __init__(self, *args, **kwds):
        Component.__init__(self, *args, **kwds)

        print("[Active_tag] initializing component")

        # Set up data structures
        self.tags = {}
        self.scan_tags()
        self.generated = False

    def scan_tags(self):
        """ scan through all Content objects, collecting tags """
        print("[Active_tag] building tag database")
        for c in self.data.content['blog']:
            if "tag" not in c.metadata:
                continue
            tags = c.metadata["tag"].split(" ")
            for t in tags:
                if t not in self.tags:
                    self.tags[t] = []
                self.tags[t].append(c)
    def create_tag_page(self, tag):
        print("[Active_tag] Generating tag page for {}".format(tag))
        a = Tag_page(self.data)
        a.content = sorted(self.tags[tag],key=lambda c: c.published,reverse=True)
        fields = {}
        fields['posts'] = a.render()
        fields['title'] = "blog > tagged '{}'".format(tag)
        output = self.data.render_template("blog.tmpl.html", fields)
        relpath = os.path.join("blog","tag",tag + ".html")
        filepath = os.path.join(self.data.output_dir, relpath)
        self.data.write_file(filepath, output)
        return relpath

    def tag_to_tag_links(self, tags):
        tag_link = "<a href=\"/blog/tag/{}.html\">{}</a> "
        return " ".join(map(lambda x: tag_link.format(x,x),tags))

    def render(self, tmpl_name=None, fields=None, **kwds):
        # if this is the first time rendering, gen tag pages
        if not self.generated:
            print("[Active_tag] creating tag listing pages")
            self.generated = True
            # Generate tag page listings
            for tag in self.tags:
                self.create_tag_page(tag)
        if fields is None or "tag" not in fields:
            return ""
        tags = fields["tag"].split(" ")
        return self.tag_to_tag_links(tags)

