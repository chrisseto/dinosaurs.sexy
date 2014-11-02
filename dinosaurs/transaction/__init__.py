from peewee import IntegrityError

from dinosaurs import api
from dinosaurs import settings
from dinosaurs.transaction.coin import get_cost
from dinosaurs.exceptions import AddressReserved
from dinosaurs.exceptions import InvalidEmailError
from dinosaurs.exceptions import AddressTakenError
from dinosaurs.exceptions import InvalidDomainError
from dinosaurs.transaction.coin import check_balance
from dinosaurs.exceptions import PaymentRequiredError
from dinosaurs.transaction.database import Transaction


def validate_email(address):
    return True  # TODO


def resolve_transaction(transaction):
    balance = check_balance(transaction.address)
    if transaction - balance > 0:
        raise PaymentRequiredError(transaction.cost - balance)

    connection = api.get_connection(transaction.domain)
    passwd = api.create_email(connection, transaction.email)

    transaction.temp_pass = passwd
    transaction.is_complete = True

    return passwd


def create_transaction(email, domain):
    if domain not in settings.DOMAINS.keys():
        raise InvalidDomainError(domain)

    if not validate_email(email):
        raise InvalidEmailError(email)

    model = Transaction(email=email, domain=domain, cost=get_cost())
    try:
        model.save()
    except IntegrityError:
        model = Transaction.get(
            (Transaction.email == email) &
            (Transaction.domain == domain)
        )

        if model.is_complete:
            raise AddressTakenError('%s@%s' % (email, domain))

        if model.expired:
            model.reset_transaction()
            return model

        raise AddressReserved('%s@%s' % (email, domain), model.seconds_left)

    return model


def get_transaction(tid):
    return Transaction.get(Transaction.tid == tid)
