"""Tests for Accela Records package"""
import json
from unittest.mock import patch
from accela_rest_sdk.accela import Accela

TEST_CONFIG = {
    'APP_ID' : '123',
    'APP_SECRET' : 'ABC',
    'AGENCY' : 'AGENCY'
}

def test_get_records():
    """ test get_records """
    with open('tests/mocks/records.json', 'r') as file_obj:
        mock_records = json.load(file_obj)

    assert mock_records

    if mock_records:
        accela = Accela(TEST_CONFIG)

        with patch('accela_rest_sdk.accela_rest.rest_client.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = mock_records
            response = accela.records.get_records("AGENCY-ABCDEF-00000-00123", None, 'AccessToken')

        assert mock_records == response.json()
