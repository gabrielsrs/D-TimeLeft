import pytest
from werkzeug.test import Client
from pymongo import MongoClient


@pytest.fixture
def client():
    from app import app

    test_mongodb_uri = 'mongodb://localhost/test'

    app.config.update({
        "MONGO_CONNECTION": test_mongodb_uri,
        "TESTING": True,
    })

    test_client = Client(app)

    yield test_client

    mongo = MongoClient(test_mongodb_uri)
    mongo.drop_database('test')
