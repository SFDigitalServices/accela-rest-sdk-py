""" SDK module """
# pylint: disable=relative-beyond-top-level
from .accela_rest.rest_client import AccelaRestClient
from .accela_rest.records import AccelaRestRecords

class Accela():
    # pylint: disable=too-few-public-methods
    """ SDK class """
    def __init__(self, config):
        self.client = AccelaRestClient(config)
        self.records = AccelaRestRecords(self.client)
