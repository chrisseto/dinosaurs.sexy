import os
import json
import httplib as http

import tornado.web
import tornado.ioloop

from dinosaurs import api
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


class EmailAPIHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        self.finish({
            "code": status_code,
            "message": self._reason,
        })

    def post(self):
        try:
            req_json = json.loads(self.request.body)
        except ValueError:
            raise tornado.web.HTTPError(http.BAD_REQUEST)

        email = req_json.get('email')
        domain = req_json.get('domain')

        connection = api.get_connection(domain)

        if not email or not domain or not connection:
            raise tornado.web.HTTPError(http.BAD_REQUEST)

        try:
            ret, passwd = api.create_email(connection, email)
        except api.YandexException as e:
            if e.message != 'occupied':
                raise
            self.write({})
            raise tornado.web.HTTPError(http.FORBIDDEN)

        self.write({
            'password': passwd,
            'email': ret['login'],
            'domain': ret['domain']
        })

        self.set_status(http.CREATED)
