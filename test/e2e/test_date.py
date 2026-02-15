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

def test_get_date(client, date):
    response = client.get(f'/date/{str(date.inserted_id)}')

    assert response.status_code == HTTPStatus.OK

def test_update_date(client, date):
    data_object = DateFactory(dateEnd=None)
    response = client.patch(f'/date/{str(date.inserted_id)}', json=asdict(data_object))

    assert response.status_code == HTTPStatus.OK
    assert response.json['data']['title'] == data_object.title

def test_delete_date(client, date):
    response = client.delete(f'/date/{str(date.inserted_id)}')

    assert response.status_code == HTTPStatus.OK
    assert response.json['message'] == 'Date deleted successfully'