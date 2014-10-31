import os
import httplib as http

import tornado.web
import tornado.ioloop

from dinosaurs import api
from dinosaurs import util
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


class EmailAPIHandler(util.JSONApiHandler):
    ARGS = {
        'POST': ['email', 'domain']
    }

    def post(self):
        email = self.json['email']
        domain = self.json['domain']

        try:
            self.write({
                'password': util.create_email(email, domain)
            })
            self.set_status(http.CREATED)
        except AddressTakenError as e:
            raise tornado.web.HTTPError(http.BAD_REQUEST, reason='taken')
        except PaymentRequiredError as e:
            self.set_status(http.PAYMENT_REQUIRED)
            self.write({
                'address': address,
                'amount': 500
            })
        except api.YandexException as e:
            self.write({})
            raise tornado.web.HTTPError(http.FORBIDDEN)
