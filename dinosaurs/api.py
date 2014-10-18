import random
import string

from collections import namedtuple

import requests

from dinosaurs import settings


QUERY_TEMPLATE = '?token={}&domain={}'
BASE_URL = 'https://pddimp.yandex.ru/api2/'

Connection = namedtuple('Connection', ['auth', 'domain'])


class YandexException(Exception):
    pass


rndstr = lambda: ''.join(random.sample(string.ascii_letters + string.hexdigits, 17))


def get_connection(domain):
    try:
        key = settings[domain]
        return Connection(auth=key, domain=domain)
    except KeyError:
        return None


def _check_error(ret_json):
    if ret_json.get('success') == 'error':
        raise YandexException(ret_json['error'])


def list_emails(connection):
    url = '{}admin/email/list'.format(BASE_URL) + QUERY_TEMPLATE.format(*connection)
    ret = requests.get(url).json()
    _check_error(ret)
    return ret


def create_email(connection, email, password=None):
    if not password:
        password = rndstr()

    url = '{}admin/email/add'.format(BASE_URL) + QUERY_TEMPLATE.format(*connection)

    url += '&login={}&password={}'.format(email, password)

    ret = requests.post(url).json()

    _check_error(ret)

    return ret, password


def delete_email(connection, email=None, uid=None):
    if not email and uid:
        raise YandexException('Must specify email or uid')

    url = '{}admin/email/del'.format(BASE_URL) + QUERY_TEMPLATE.format(*connection)

    if email:
        url += '&login={}'.format(email)
    else:
        url += '&uid={}'.format(uid)

    ret = requests.post(url).json()

    _check_error(ret)

    return ret
