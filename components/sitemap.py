from components import Component
class Sitemap(Component):
    def render(self, *args, **kwds):
        if not hasattr(self, "rendered"):
            self.rendered = ""
            ctype = 'page'
            link = "<li><a href=\"{}\">{}</a><?li>\n"
            for c in self.data.content[ctype]:
                if "slug" in c.metadata:
                    url = "/{}/{}.html".format(ctype,c.metadata['slug'][0])
                else:
                    url = "/{}/{}.html".format(ctype.c.name)
                self.rendered += link.format(url, c.metadata['title'][0])
        return self.rendered
