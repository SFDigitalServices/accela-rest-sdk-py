""" SDK module """
class AccelaRestRecords():
    # pylint: disable=too-few-public-methods
    """ Accela REST Records Class """
    def __init__(self, client, path_base='/v4/records'):
        self.client = client
        self.path_base = path_base

    def get_records(self, record_ids, params=None, auth_type='AccessToken'):
        """ Gets the requested record(s). """
        path = self.path_base + '/' + record_ids
        return self.client.get(path, params, auth_type)
