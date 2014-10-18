import os

import tornado.web
import tornado.ioloop


class SingleStatic(tornado.web.StaticFileHandler):
    def initialize(self, path):
        self.dirname, self.filename = os.path.split(path)
        super(SingleStatic, self).initialize(self.dirname)

    def get(self, path=None, include_body=True):
        super(SingleStatic, self).get(self.filename, include_body)
