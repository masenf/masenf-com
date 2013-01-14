from components import Component

class Rss2(Component):
    """ generate an rss2 feed for the site

        rendering this component generates the rss
        feed, if not created, and returns a <link>
        tag. put the replacement in the HEAD of the document"""
    def __init__(self, *args, **kwds):
        Component.__init__(self, *args, **kwds)

        self.siteroot = "http://masenf.com"
        self.rsstitle = "masenf.com > blog"
        self.rssfile = "output/feed.rss"
        self.rsspath = "/feed.rss"
        self.NUM_POSTS = 20
        self.PREVIEW_CHARS = 256
        self.output_rss(self.rssfile)
    def output_rss(self, filename):
        self.log("Generating RSS2 feed for site at {}".format(self.rssfile), self.data.level)
        import PyRSS2Gen as rss2
        import htmltruncate
        import datetime
        items = []
        posts = sorted(self.data.content['blog'], key=lambda c: c.published, reverse=True)[0:self.NUM_POSTS]
        for c in posts:
            try:
                description = htmltruncate.truncate(c.render(),self.PREVIEW_CHARS,"...")
            except htmltruncate.UnbalancedError:
                self.log("Posts", "Error truncating {}, ensure proper document structure".format(post.name), self.data.level)
                raise
            link = self.siteroot + c.metadata['link']
            items.append(rss2.RSSItem(
                title = c.metadata['title'],
                description = description,
                link = link,
                guid = rss2.Guid(link),
                pubDate = c.metadata['published']
            ))
        rss = rss2.RSS2(
            title = self.rsstitle,
            link = "http://masenf.com/",
            description = "Latests posts about the life of Masen Furer",
            lastBuildDate = datetime.datetime.utcnow(),
            items = items
        )
        with open(filename,'w') as f:
            f.write(rss.to_xml())
    def render(self, *args, **kwds):
        link = "<link rel=\"alternate\" type=\"application/rss+xml\" title=\"{}\" href=\"{}\" />"
        return link.format(self.rsstitle, self.rsspath)
