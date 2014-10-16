from collections import namedtuple

import requests


QUERY_TEMPLATE = '?token={}&domain={}'
BASE_URL = 'https://pddimp.yandex.ru/api2/'

Connection = namedtuple('Connection', ['auth', 'domain'])


def list_emails(connection):
    url = '{}admin/email/list'.format(BASE_URL) + QUERY_TEMPLATE.format(*connection)
    ret = requests.get(url)
    return ret.json()
