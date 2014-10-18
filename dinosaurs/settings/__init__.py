from dinosaurs.api import Connection
from dinosaurs.settings.defaults import *
from dinosaurs.settings.local import *


connections = [
    Connection(auth=token, domain=domain)
    for token, domain
    in DOMAINS.items()
]
