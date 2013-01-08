class Component(object):
    def __init__(self, data):
        self.data = data
        self.log = self.data.log
    def render(self, *args, **kwds):
        return "Empty Component"
