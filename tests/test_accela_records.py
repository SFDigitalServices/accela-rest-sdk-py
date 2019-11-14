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

def test_create_record():
    """ test create_record """
    with open('tests/mocks/create_record.json', 'r') as file_obj:
        create_record_data = json.load(file_obj)

    assert create_record_data

    with open('tests/mocks/create_record_response.json', 'r') as file_obj:
        create_record_response = json.load(file_obj)

    assert create_record_response

    if create_record_data and create_record_response:
        accela = Accela(TEST_CONFIG)
        with patch('accela_rest_sdk.accela_rest.rest_client.requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = create_record_response

            params = {'fields':'customId,id'}
            response = accela.records.create_record(create_record_data, params)

        assert create_record_response == response.json()
