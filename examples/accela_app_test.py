# pylint: disable=redefined-outer-name
"""Tests for examples/accela_app.py"""
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
    response = client.simulate_get(
        '/page/get_records',
        params={'ids':'CCSF-18CAP-00000-008YI', 'expand':'customTables,customForms'})
    assert response.status_code == 200

    content = json.loads(response.content)

    assert content
    assert 'result' in content

    response = content['result'][0]

    possible_keys = ['name', 'status', 'id', 'description', 'customTables', 'customForms']
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
            record_id = content['result']['id']
            assert 'customId' in content['result']

            # Test update_record
            with open('tests/mocks/update_record.json', 'r') as file_obj:
                mock_update = json.load(file_obj)

            assert mock_update
            response = client.simulate_put(
                '/page/update_record',
                params={'id':record_id},
                body=json.dumps(mock_update))
            assert response.status_code == 200
            content = json.loads(response.content)
            if 'status' in content:
                assert content['status'] == 200

            # Test update_record_custom_tables
            with open('tests/mocks/update_record_custom_tables.json', 'r') as file_obj:
                mock_custom_tables = json.load(file_obj)

            assert mock_custom_tables
            response = client.simulate_put(
                '/page/update_record_custom_tables',
                params={'id':record_id},
                body=json.dumps(mock_custom_tables))
            assert response.status_code == 200
            content = json.loads(response.content)
            if 'status' in content:
                assert content['status'] == 200

            # Test update_record_custom_forms
            with open('tests/mocks/update_record_custom_forms.json', 'r') as file_obj:
                mock_custom_forms = json.load(file_obj)

            assert mock_custom_tables
            response = client.simulate_put(
                '/page/update_record_custom_forms',
                params={'id':record_id},
                body=json.dumps(mock_custom_forms))
            assert response.status_code == 200
            content = json.loads(response.content)
            if 'status' in content:
                assert content['status'] == 200

def test_create_record_empty(client):
    """ Test create_record with empty post body """
    response = client.simulate_post('/page/create_record')
    assert response.status_code == 400

def test_update_record_empty(client):
    """ Test update_record empty """
    #with empty record ids
    response = client.simulate_put('/page/update_record')
    assert response.status_code == 400

    #with empty post body
    response = client.simulate_put(
        '/page/update_record',
        params={'id':'CCSF-18CAP-00000-008YI'})
    assert response.status_code == 400

def test_error(client):
    """Test error state"""
    response = client.simulate_get('/error')
    assert response.status_code == 404

def test_default_page(client):
    """Test default page"""
    response = client.simulate_get('/page/home')
    assert response.status_code == 200
