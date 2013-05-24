from components import Component

class Rewrite(Component):

    def __init__(self, *args, **kwds):
        Component.__init__(self, *args, **kwds)

        # add predefined rewrites
        self.rewrites = { '/?' : ('/home.html',''),
                            'blog/?' : ('/blog.html','[R]'),
                            'blog/tag/([\ a-zA-Z]+)' : ('/blog/tag/$1.html','[R]'),
                            'blog/archive/([0-9]{4})-([0-9]{2})/?' : ('/blog/archive/$1-$2.html','[R]'),
                            'blog/rss2/?' : ('/feed.rss','[R]') }
        self.index_permalinks()
        self.write_htaccess()
    def index_permalinks(self):
        self.log("Rewrite","Indexing permalinks...",self.data.level)
        for ctype in self.data.content:
            for c in self.data.content[ctype]:
                if "rewrite" in c.metadata:
                    pl = c.metadata["rewrite"].split(" ")
                    for p in pl:
                        self.rewrites[p] = (c.metadata["link"],'[R]')
    def write_htaccess(self, filename="output/.htaccess"):
        self.log("Rewrite","Writing Rewrite Rules to {}...".format(filename),self.data.level)
        with open(filename, 'w') as f:
            f.write("RewriteEngine on\n")
            for pl, l in self.rewrites.iteritems():
                f.write("RewriteRule ^{}$ {} {}\n".format(pl,*l))


