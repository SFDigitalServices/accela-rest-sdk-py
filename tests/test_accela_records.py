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

def test_update_record():
    """ test update_record """
    with open('tests/mocks/update_record.json', 'r') as file_obj:
        update_record_data = json.load(file_obj)

    assert update_record_data

    with open('tests/mocks/update_record_response.json', 'r') as file_obj:
        update_record_response = json.load(file_obj)

    assert update_record_response

    if update_record_data and update_record_response:
        accela = Accela(TEST_CONFIG)
        with patch('accela_rest_sdk.accela_rest.rest_client.requests.put') as mock_put:
            mock_put.return_value.status_code = 200
            mock_put.return_value.json.return_value = update_record_response

            params = {'fields':'customId,id'}
            response = accela.records.update_record(
                "AGENCY-ABCDEF-00000-00123", update_record_data,
                params, 'AccessToken')

        assert update_record_response == response.json()

def test_update_record_custom_tables():
    """ test update_record_custom_tables """
    with open('tests/mocks/update_record_custom_tables.json', 'r') as file_obj:
        update_record_custom_tables_data = json.load(file_obj)

    assert update_record_custom_tables_data

    with open('tests/mocks/update_record_custom_tables_response.json', 'r') as file_obj:
        update_record_custom_tables_response = json.load(file_obj)

    assert update_record_custom_tables_response

    if update_record_custom_tables_data and update_record_custom_tables_response:
        accela = Accela(TEST_CONFIG)
        with patch('accela_rest_sdk.accela_rest.rest_client.requests.put') as mock_put:
            mock_put.return_value.status_code = 200
            mock_put.return_value.json.return_value = update_record_custom_tables_response

            params = None
            response = accela.records.update_record_custom_tables(
                "AGENCY-ABCDEF-00000-00123", update_record_custom_tables_data,
                params, 'AccessToken')

        assert update_record_custom_tables_response == response.json()

def test_update_record_custom_forms():
    """ test update_record_custom_forms """
    with open('tests/mocks/update_record_custom_forms.json', 'r') as file_obj:
        update_record_custom_forms_data = json.load(file_obj)

    assert update_record_custom_forms_data

    with open('tests/mocks/update_record_custom_forms_response.json', 'r') as file_obj:
        update_record_custom_forms_response = json.load(file_obj)

    assert update_record_custom_forms_response

    if update_record_custom_forms_data and update_record_custom_forms_response:
        accela = Accela(TEST_CONFIG)
        with patch('accela_rest_sdk.accela_rest.rest_client.requests.put') as mock_put:
            mock_put.return_value.status_code = 200
            mock_put.return_value.json.return_value = update_record_custom_forms_response

            params = None
            response = accela.records.update_record_custom_forms(
                "AGENCY-ABCDEF-00000-00123", update_record_custom_forms_data,
                params, 'AccessToken')

        assert update_record_custom_forms_response == response.json()

def test_create_record_comments():
    """ test create_record """
    with open('tests/mocks/create_record_comments.json', 'r') as file_obj:
        create_record_comments = json.load(file_obj)

    assert create_record_comments

    with open('tests/mocks/create_record_comments_response.json', 'r') as file_obj:
        create_record_comments_response = json.load(file_obj)

    assert create_record_comments_response

    if create_record_comments and create_record_comments_response:
        accela = Accela(TEST_CONFIG)
        with patch('accela_rest_sdk.accela_rest.rest_client.requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = create_record_comments_response

            params = {'fields':'customId,id'}
            response = accela.records.create_record_comments(
                "AGENCY-ABCDEF-00000-00123", create_record_comments, params)

        assert create_record_comments_response == response.json()
