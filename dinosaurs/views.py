import os

import tornado.web
import tornado.ioloop

from dinosaurs import settings


class SingleStatic(tornado.web.StaticFileHandler):
    def initialize(self, path):
        self.dirname, self.filename = os.path.split(path)
        super(SingleStatic, self).initialize(self.dirname)

    def get(self, path=None, include_body=True):
        super(SingleStatic, self).get(self.filename, include_body)


class DomainAPIHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({
            'availableDomains': settings.DOMAINS.keys()
        })
