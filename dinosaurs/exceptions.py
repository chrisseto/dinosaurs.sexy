# Base Exception
class DinosaurError(Exception):
    pass


class PaymentRequiredError(DinosaurError):
    pass


class YandexException(DinosaurError):
    pass


class InvalidEmailError(YandexException):
    pass


class InvalidDomainError(YandexException):
    pass


class AddressTakenError(YandexException):
    pass


class AddressReserved(YandexException):
    pass
