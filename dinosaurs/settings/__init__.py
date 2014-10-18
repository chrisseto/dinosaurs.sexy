from dinosaurs.api import Connection
from dinosaurs.settings.defaults import *
from dinosaurs.settings.local import *


connection = Connection(auth=TOKEN, domain=DOMAIN)
