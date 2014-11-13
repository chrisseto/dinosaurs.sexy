# Base Exception
class DinosaurError(Exception):
    pass


class NoCoinServerError(DinosaurError):
    pass


class NoSuchTransactionError(DinosaurError):
    pass


class PaymentRequiredError(DinosaurError):
    def __init__(self, delta):
        self.delta = delta
        super(PaymentRequiredError, self).__init__('%d more units required.' % delta)


class YandexException(DinosaurError):
    pass


class InvalidEmailError(YandexException):
    pass


class InvalidDomainError(YandexException):
    pass


class AddressTakenError(YandexException):
    pass


class AddressReserved(YandexException):
    def __init__(self, address, time_left):
        self.time_left = time_left
        self.email = address
        super(AddressReserved, self).__init__('Address %s is unavailable for %d more seconds' % (address, time_left))
