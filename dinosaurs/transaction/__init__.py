from dinosaurs.exceptions import PaymentRequiredError
from dinosaurs.transaction.database import Transaction


def check_transaction(transaction):
    balance = check_balance(transaction.address)
    if transaction - balance > 0:
        raise PaymentRequiredError(transaction.cost - balance)
    return True


def create_transaction(email, domain):
    model = Transaction.get(
        Transaction.email == email &
        Transaction.domain == domain
    )

    if not model:
        model = Transaction(email=email, domain=domain)
        model.save()

    return model
