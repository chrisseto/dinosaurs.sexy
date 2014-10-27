from peewee import *

db = SqliteDatabase('emails.db')


class Transaction(Model):
    cost = FloatField()
    address = CharField()
    tempPass = CharField()
    domain = CharField(index=True)
    email = CharField(primary_key=True, unique=True)
    is_complete = BooleanField(default=False, index=True)

    class Meta:
        database = db
