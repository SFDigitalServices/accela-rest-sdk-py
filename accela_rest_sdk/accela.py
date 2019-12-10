""" Python module for interacting with the Accela Construct API """
# pylint: disable=relative-beyond-top-level
from .accela_rest.rest_client import AccelaRestClient
from .accela_rest.records import AccelaRestRecords

class Accela():
    # pylint: disable=too-few-public-methods
    """ Accela class """
    def __init__(self, config):
        """
        | Declare Accela class

        :param config: Configuration
        :type config: dict
        """
        self.client = AccelaRestClient(config)
        self.records = AccelaRestRecords(self.client)
