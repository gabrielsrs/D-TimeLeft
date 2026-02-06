from http import HTTPStatus

def test_list_timezones(client):
    response = client.get('timezones')

    assert response.status_code == HTTPStatus.OK