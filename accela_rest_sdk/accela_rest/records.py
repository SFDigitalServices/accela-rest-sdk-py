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

    def update_record(self, record_id, record,
                      params=None, auth_type='AccessToken'):
        """
        | Updates details for the specified record.

        Construct API reference:
        https://developer.accela.com/docs/api_reference/api-records.html#operation/v4.put.records.id

        :param record_id: The ID of the record to fetch.
        :type record_id: str
        :param record: Record information to be updated.
        :type record: dict
        :param params: Query Parameters
        :type params: dict, optional
        :param auth_type: Authentication type
        :type auth_type: str, optional
        :return: return from AccelaRestClient.put
        """
        path = self.path_base + '/' + record_id
        return self.client.put(path, record, params, auth_type)

    def update_record_custom_tables(self, record_id, custom_tables,
                                    params=None, auth_type='AccessToken'):
        """
        | Updates the custom table for the specified record.

        Construct API reference:
        https://developer.accela.com/docs/api_reference/api-records.html#operation/v4.put.records.recordId.customTables

        :param record_id: The ID of the record to fetch.
        :type record_id: str
        :param custom_tables: Custom table data to be updated.
        :type custom_tables: array
        :param params: Query Parameters
        :type params: dict, optional
        :param auth_type: Authentication type
        :type auth_type: str, optional
        :return: return from AccelaRestClient.put
        """
        path = self.path_base + '/' + record_id + '/customTables'
        return self.client.put(path, custom_tables, params, auth_type)

    def update_record_custom_forms(self, record_id, custom_forms,
                                   params=None, auth_type='AccessToken'):
        """
        | Updates the custom forms for the specified record.

        Construct API reference:
        https://developer.accela.com/docs/api_reference/api-records.html#operation/v4.put.records.recordId.customForms

        :param record_id: The ID of the record to fetch.
        :type record_id: str
        :param custom_forms: Custom table data to be updated.
        :type custom_forms: array
        :param params: Query Parameters
        :type params: dict, optional
        :param auth_type: Authentication type
        :type auth_type: str, optional
        :return: return from AccelaRestClient.put
        """
        path = self.path_base + '/' + record_id + '/customForms'
        return self.client.put(path, custom_forms, params, auth_type)

    def create_record_comments(self, record_id, comments, params=None, auth_type='AccessToken'):
        """
        | Add comments to a record.

        Construct API reference:
        https://developer.accela.com/docs/api_reference/api-records.html#operation/v4.get.records.recordId.comments
        :param record_id: The ID of the record to fetch.
        :type record_id: str
        :param comments: The comments to be added.
        :type comments: array
        :param params: Query Parameters
        :type params: dict, optional
        :param auth_type: Authentication type
        :type auth_type: str, optional
        :return: return from AccelaRestClient.post
        """
        path = self.path_base + '/' + record_id + '/comments'
        return self.client.post(path, comments, params, auth_type)
