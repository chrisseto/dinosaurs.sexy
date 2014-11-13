import os
import httplib as http

import tornado.web

from dinosaurs import util
from dinosaurs import settings
from dinosaurs import exceptions
from dinosaurs import transaction


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


class TransactionAPIHandler(util.JSONApiHandler):
    ARGS = {
        'POST': ['email', 'domain']
    }

    def post(self):
        email = self.json['email']
        domain = self.json['domain']

        try:
            self.set_status(http.CREATED)
            self.write({
                'id': transaction.create_transaction(email, domain).tid
            })
        except exceptions.AddressReserved as e:
            self.set_status(http.BAD_REQUEST)
            self.write({
                'reason': 'reserved',
                'timeLeft': e.time_left
            })
            return
        except exceptions.NoCoinServerError:
            raise tornado.web.HTTPError(http.SERVICE_UNAVAILABLE)
        except exceptions.AddressTakenError:
            raise tornado.web.HTTPError(http.BAD_REQUEST, reason='taken')
        except exceptions.InvalidEmailError:
            raise tornado.web.HTTPError(http.BAD_REQUEST, reason='invalid email')
        except exceptions.InvalidDomainError:
            raise tornado.web.HTTPError(http.BAD_REQUEST, reason='invalid domain')


class EmailAPIHandler(util.JSONApiHandler):
    def get(self, transaction_id):
        try:
            t = transaction.get_transaction(transaction_id)

            if not t:
                raise tornado.web.HTTPError(http.NOT_FOUND)

            transaction.resolve_transaction(t)
        except exceptions.PaymentRequiredError as e:
            self.set_status(http.PAYMENT_REQUIRED)
            self.write({
                'address': t.address,
                'amount': t.cost,
                'delta': e.delta,
                'secondsLeft': t.seconds_left
            })
            return
        except exceptions.NoSuchTransactionError:
            raise tornado.web.HTTPError(http.NOT_FOUND)
        except exceptions.NoCoinServerError:
            raise tornado.web.HTTPError(http.SERVICE_UNAVAILABLE)

        self.set_status(http.CREATED)
        self.write({'password': t.temp_pass})
