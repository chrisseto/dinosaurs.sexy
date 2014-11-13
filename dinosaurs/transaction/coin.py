from socket import error
from httplib import HTTPException

import dogecoinrpc

from dinosaurs.exceptions import NoCoinServerError

connection = dogecoinrpc.connect_to_local()


def requires_connection(func):
    def wraps(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (HTTPException, error):
            raise NoCoinServerError()
    return wraps


def get_cost():
    return 1


@requires_connection
def generate_address():
    return connection.getnewaddress()


@requires_connection
def check_balance(addr):
    return float(connection.getbalance(addr))
