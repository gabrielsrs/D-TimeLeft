from http import HTTPStatus
from dataclasses import asdict

from ..fixtures.data_factories.date_factory import DateFactory

def test_create_date(client):
    response = client.post('date', json={
        'title': 'test',
        'dateEnd': '2026-02-05T05:14:40.754Z',
        'timezone': 'Brazil/West'
    })

    assert response.status_code == HTTPStatus.CREATED

def test_create_date_with_wrong_tz(client):
    response = client.post('date', json={
        'title': 'test',
        'dateEnd': '2026-02-05T05:14:40.754Z',
        'timezone': 'Wrong/One'
    })

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json['message'] == 'Input payload validation failed'
    assert response.json['errors'] == {'timezone': 'Invalid tz identifier "Wrong/One"'}

def test_get_date(client, date):
    response = client.get(f'/date/{str(date.inserted_id)}')

    assert response.status_code == HTTPStatus.OK

def test_get_date_with_wrong_id_type(client):
    response = client.get('/date/1')

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json['message'] == 'Invalid date Id'

def test_get_date_with_non_created_id(client):
    response = client.get('/date/69927ca51081d95a880634ed')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json['message'] == 'Id not found'

def test_update_date(client, date):
    data_object = DateFactory(dateEnd=None)
    response = client.patch(f'/date/{str(date.inserted_id)}', json=asdict(data_object))

    assert response.status_code == HTTPStatus.OK
    assert response.json['data']['title'] == data_object.title

def test_update_date_with_nothing_to_update(client, date):
    response = client.patch(f'/date/{str(date.inserted_id)}', json={})

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json['message'] == 'Nothing to update'

def test_update_date_without_current_data(client):
    data_object = DateFactory(dateEnd=None)
    response = client.patch('/date/69927ca51081d95a880634ed', json=asdict(data_object))

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json['message'] == 'Informed Id not return any registered date'

def test_delete_date(client, date):
    response = client.delete(f'/date/{str(date.inserted_id)}')

    assert response.status_code == HTTPStatus.OK
    assert response.json['message'] == 'Date deleted successfully'

def test_delete_date_with_wrong_id_type(client):
    response = client.delete('/date/1')

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json['message'] == 'Invalid date Id'

def test_delete_date_with_non_created_id(client):
    response = client.delete('/date/69927ca51081d95a880634ed')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json['message'] == 'Id not found'