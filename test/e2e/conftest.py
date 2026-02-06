import pytest
from dataclasses import asdict

from ..fixtures.db import client, collection
from ..fixtures.data_factories.date_db_factory import DateDbFactory


@pytest.fixture
def date(collection):
    date_object = DateDbFactory()
    data = collection.insert_one(asdict(date_object))

    return data