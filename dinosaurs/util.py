import json
import random
import string
import httplib as http

import tornado.web

from dinosaurs import api

from dinosaurs.transaction import check_payment
from dinosaurs.transaction import get_transaction

from dinosaurs.exceptions import AddressReserved
from dinosaurs.exceptions import AddressTakenError
from dinosaurs.exceptions import PaymentRequiredError


rndstr = lambda: ''.join(random.sample(string.ascii_letters + string.hexdigits, 17))


def create_email(address, domain, client_secret):
    transaction = get_transaction(address)

    if transaction.is_complete:
        raise AddressTakenError()

    if transaction.secret != client_secret and not transaction.expired:
        raise AddressReserved(address)

    check_payment(transaction)

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
            except ValueError:
                raise tornado.web.HTTPError(http.BAD_REQUEST)

    def write_error(self, status_code, **kwargs):
        self.finish({
            "code": status_code,
            "message": self._reason,
        })
