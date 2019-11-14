# pylint: disable=redefined-outer-name
"""Tests for boilerplate/accela_app.py"""
import json
import pytest
from falcon import testing
import examples.accela_app

@pytest.fixture()
def client():
    """ client fixture """
    return testing.TestClient(examples.accela_app.run())

def test_get_posts(client):
    """ Test get_posts """
    response = client.simulate_get('/page/get_records', params={'ids':'CCSF-18CAP-00000-008YI'})
    assert response.status_code == 200

    content = json.loads(response.content)

    assert content
    assert 'result' in content

    response = content['result'][0]

    possible_keys = ['name', 'status', 'id', 'description']
    assert len(list(set(response.keys() & possible_keys))) == len(possible_keys)

def test_get_posts_missing_ids(client):
    """ Test get_posts without ids """
    response = client.simulate_get('/page/get_records')
    assert response.status_code == 400

def test_create_record(client):
    """ Test create_record """
    with open('tests/mocks/create_record.json', 'r') as file_obj:
        mock_record = json.load(file_obj)

    assert mock_record

    if mock_record:
        response = client.simulate_post('/page/create_record', body=json.dumps(mock_record))
        assert response.status_code == 200
        content = json.loads(response.content)
        assert 'result' in content
        if 'result' in content:
            assert 'id' in content['result']
            assert 'customId' in content['result']

def test_create_record_empty(client):
    """ Test create_record with empty post body """
    response = client.simulate_post('/page/create_record')
    assert response.status_code == 400

def test_error(client):
    """Test error state"""
    response = client.simulate_get('/error')
    assert response.status_code == 404

def test_default_page(client):
    """Test default page"""
    response = client.simulate_get('/page/home')
    assert response.status_code == 200
