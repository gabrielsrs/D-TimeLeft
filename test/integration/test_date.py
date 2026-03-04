from src.handlers.create_date_handler import CreateDateHandler
from src.handlers.get_date_handler import GetDateHandler
from src.handlers.update_date_handler import UpdateDateHandler
from src.handlers.delete_date_handler import DeleteDateHandler
from ..fixtures.data_factories.date_factory import DateFactory
from dataclasses import asdict


def test_create_date(collection):
    create_date_handler = CreateDateHandler()
    data_object = DateFactory()

    created_date = create_date_handler.create_date(asdict(data_object), asdict(data_object))

    assert created_date[1] == 201
    assert created_date[0]["message"] == "Date successfully created"
    assert created_date[0]["data"]["id"]
    assert created_date[0]["data"]["title"] == data_object.title

def test_get_date(collection, date):
    get_date_handler = GetDateHandler(str(date[0].inserted_id))

    get_date = get_date_handler.get_date()

    assert get_date["code"] == 200
    assert get_date["data"]["id"] == str(date[0].inserted_id)
    assert get_date["data"]["title"] == date[1].title

def test_update_date(collection, date):
    update_date_handler = UpdateDateHandler(str(date[0].inserted_id))
    data_object = DateFactory()

    updated_date = update_date_handler.update_date(asdict(data_object), asdict(data_object))

    assert updated_date[1] == 200
    assert updated_date[0]["message"] == "Object successfully updated"
    assert updated_date[0]["data"]["id"]
    assert updated_date[0]["data"]["title"] == data_object.title

def test_delete_date(collection, date):
    delete_date_handler = DeleteDateHandler(str(date[0].inserted_id))

    deleted_date = delete_date_handler.delete_date()

    assert deleted_date[1] == 200
    assert deleted_date[0]["deletedId"] == str(date[0].inserted_id)
