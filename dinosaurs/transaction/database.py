from datetime import datetime

from peewee import *

from dinosaurs import settings
from dinosaurs.transaction.coin import generate_address


db = SqliteDatabase(settings.database)


class Transaction(Model):
    cost = FloatField()
    address = CharField()
    started = DateField()
    tempPass = CharField()
    domain = CharField(index=True)
    email = CharField(primary_key=True, unique=True)
    is_complete = BooleanField(default=False, index=True)

    class Meta:
        database = db

    def __init__(self, *args, **kwargs):
        kwargs['started'] = datetime.now()
        kwargs['address'] = generate_address()
        super(Transaction, self).__init__(*args, **kwargs)

    @property
    def expired(self):
        return (datetime.now() - self.started).minutes > 4

    @property
    def seconds_left(self):
        return (datetime.now() - self.started).total_seconds
