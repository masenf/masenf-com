from components import Component
import htmltruncate

class Posts(Component):
    def __init__(self, *args, **kwds):
        Component.__init__(self, *args, **kwds)
        self.PREVIEW_CHARS = 512
        self.TEMPLATE = "post-short.tmpl.html"
        self.NUM_POSTS = 10
    def get_content(self):
        """ overload this function to filter the dataset,
            returns a list of Content """
        return sorted(self.data.content['blog'], key=lambda c: c.published, reverse=True)[0:self.NUM_POSTS]

    def render(self, *args, **kwds):
        if not hasattr(self,"rendered"):
            self.rendered = ""
            # copy all blogposts
            loc_content = self.get_content()
            for post in loc_content:
                fields = self.data.flatten_metadata(post.metadata)
                fields['link'] = "/{}/{}.html".format(post.ctype,post.name)
                try:
                    fields['body'] = htmltruncate.truncate(post.content,self.PREVIEW_CHARS,"...")
                except htmltruncate.UnbalancedError:
                    print("Error truncating {}, ensure proper document structure".format(post.name))
                    raise
                self.rendered += self.data.render_template(self.TEMPLATE, fields)
        return self.rendered
