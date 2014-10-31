import json
import httplib as http

import tornado.web

from dinosaurs import api
from dinosaurs.exceptions import AddressReserved
from dinosaurs.transaction import get_transaction
from dinosaurs.exceptions import AddressTakenError
from dinosaurs.transaction import check_transaction


def create_email(address, domain, client_secret):
    transaction = get_transaction(address)

    if transaction.is_complete:
        raise AddressTakenError()

    if transaction.secret != client_secret and not transaction.expired:
        raise AddressReserved(address)

    check_transaction(transaction)

    connection = api.get_connection(domain)
    _, passwd = api.create_email(connection, address)

    return passwd


class JSONApiHandler(tornado.web.RequestHandler):
    def prepare(self, *args, **kwargs):
        for key in self.ARGS[self.request.method]:
            if not self.json.get(key):
                raise tornado.web.HTTPError(
                    http.BAD_GATEWAY,
                    message='Missing required argument % s' % key
                )

    @property
    def json(self):
        try:
            return self._json
        except AttributeError:
            try:
                self._json = json.loads(self.request.body)
                return self._json
            except ValueError:
                raise tornado.web.HTTPError(http.BAD_REQUEST)

    def write_error(self, status_code, **kwargs):
        self.finish({
            "code": status_code,
            "message": self._reason,
        })
