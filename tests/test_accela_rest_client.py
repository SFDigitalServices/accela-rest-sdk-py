"""Tests for Accela Rest Client package"""
import json
from unittest.mock import patch
from unittest import TestCase
from accela_rest_sdk.accela import Accela

TEST_CONFIG = {
    'APP_ID' : '123',
    'APP_SECRET' : 'ABC',
    'AGENCY' : 'AGENCY'
}

def test_get_token():
    """ test get_token """
    with open('tests/mocks/token.json', 'r') as file_obj:
        mock_token = json.load(file_obj)

    assert mock_token

    if mock_token:

        accela = Accela(TEST_CONFIG)
        username = 'USER'
        password = 'PASS'
        scope = 'none'
        environment = 'TEST'

        with patch('accela_rest_sdk.accela_rest.rest_client.requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = mock_token
            response = accela.client.get_token(username, password, scope, environment)
        assert mock_token == response

        with patch('accela_rest_sdk.accela_rest.rest_client.requests.post') as mock_post:
            mock_post.return_value.status_code = 400
            mock_post.return_value.text.return_value = 'ERROR'
            test_case = TestCase()
            with test_case.assertRaises(ValueError):
                response = accela.client.get_token(username, password, scope, environment)


def test_set_auth_type():
    """ test set_auth_type """
    accela = Accela(TEST_CONFIG)

    headers = accela.client.set_auth_type('AccessToken')

    assert  'Authorization' in headers

    headers = accela.client.set_auth_type('AppCredentials')
    assert  headers['x-accela-appid'] == TEST_CONFIG['APP_ID']
    assert  headers['x-accela-appsecret'] == TEST_CONFIG['APP_SECRET']

    headers = accela.client.set_auth_type('NoAuth')
    assert  headers['x-accela-appid'] == TEST_CONFIG['APP_ID']
    assert  headers['x-accela-agency'] == TEST_CONFIG['AGENCY']
    assert  'x-accela-environment' in headers
