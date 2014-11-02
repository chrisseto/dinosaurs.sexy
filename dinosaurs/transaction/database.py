import random
import string
from datetime import datetime

from peewee import *

from dinosaurs import settings
from dinosaurs.transaction.coin import generate_address


db = SqliteDatabase(settings.DATABASE)
characters = string.ascii_lowercase + string.hexdigits


class Transaction(Model):
    tid = CharField()
    cost = FloatField()
    address = CharField()
    started = DateTimeField()
    temp_pass = CharField(null=True)
    email = CharField(index=True)
    domain = CharField(index=True)
    is_complete = BooleanField(default=False, index=True)

    class Meta:
        database = db
        indexes = ((('email', 'domain'), True),)

    def __init__(self, *args, **kwargs):
        kwargs['started'] = datetime.now()
        kwargs['address'] = generate_address()
        kwargs['tid'] = ''.join(random.sample(characters, 20))
        super(Transaction, self).__init__(*args, **kwargs)

    @property
    def expired(self):
        return not self.is_complete and self.seconds_left < 0

    @property
    def seconds_left(self):
        return (60 * 5) - (datetime.now() - self.started).total_seconds()

    def reset_transaction(self):
        self.started = datetime.now()
        self.tid = ''.join(random.sample(characters, 20))
