from components import Component
class Popular_links(Component):
    def render(self, *args, **kwds):
        if not hasattr(self, "rendered"):
            popular = []
            for ctype in self.data.content:
                for c in self.data.content[ctype]:
                    if "tag" in c.metadata:
                        tags = c.metadata["tag"].split(" ")
                        if "popular" in tags:
                            if "slug" in c.metadata:
                                url = "/{}/{}.html".format(ctype,c.metadata['slug'])
                            else:
                                url = "/{}/{}.html".format(ctype.c.name)
                            popular.append((url, c.metadata['title']))
            self.rendered = ""
            for url,title in popular:
                self.rendered += "<li><a href=\"{}\">{}</a></li>\n".format(url,title)
        return self.rendered
