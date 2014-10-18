import logging

import tornado.web
import tornado.ioloop

from dinosaurs import views
from dinosaurs import settings


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    application = tornado.web.Application([
        (r'/api/v1/domains', views.DomainAPIHandler),
        (r'/api/v1/emails', views.EmailAPIHandler),
        (r'/', views.SingleStatic, {'path': 'static/index.html'}),
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
    ], debug=settings.DEBUG)

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
