from components import Component
class Popular_links(Component):
    def render(self):
        if not hasattr(self, "rendered"):
            popular = []
            for ctype in self.data.content:
                for c in self.data.content[ctype]:
                    if "tag" in c.metadata:
                        if "popular" in c.metadata["tag"]:
                            if "slug" in c.metadata:
                                url = "/{}/{}.html".format(ctype,c.metadata['slug'][0])
                            else:
                                url = "/{}/{}.html".format(ctype.c.name)
                            popular.append((url, c.metadata['title'][0]))
            self.rendered = ""
            for url,title in popular:
                self.rendered += "<li><a href=\"{}\">{}</a></li>\n".format(url,title)
        return self.rendered
