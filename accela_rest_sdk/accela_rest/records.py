"""
Accela REST Records module

Interacts with Construct APIs for transactional records and related record resources
https://developer.accela.com/docs/api_reference/api-records.html
"""
class AccelaRestRecords():
    # pylint: disable=too-few-public-methods
    """
    | Declare Accela REST Records Class

    :param client: Accela Rest Client
    :type client: AccelaRestClient
    :param path_base: Records Base Path
    :type path_base: str
    """
    def __init__(self, client, path_base='/v4/records'):
        self.client = client
        self.path_base = path_base

    def get_records(self, record_ids, params=None, auth_type='AccessToken'):
        """
        | Gets the requested record(s).

        Contruct API reference:
        https://developer.accela.com/docs/api_reference/api-records.html#operation/v4.get.records.ids

        :param record_ids: Comma-delimited IDs of the records to fetch.
        :type record_ids: str
        :param params: Query Parameters
        :type params: dict, optional
        :param auth_type: Authentication type
        :type auth_type: str, optional
        :return: return from AccelaRestClient.get
        """
        path = self.path_base + '/' + record_ids
        return self.client.get(path, params, auth_type)

    def create_record(self, record, params=None, auth_type='AccessToken'):
        """
        | Creates a new, full record

        Construct API reference:
        https://developer.accela.com/docs/api_reference/api-records.html#operation/v4.post.records

        :param record: The create record information to be added.
        :type record: dict
        :param params: Query Parameters
        :type params: dict, optional
        :param auth_type: Authentication type
        :type auth_type: str, optional
        :return: return from AccelaRestClient.post
        """
        path = self.path_base
        return self.client.post(path, record, params, auth_type)
