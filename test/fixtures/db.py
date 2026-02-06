import pytest
from werkzeug.test import Client
from pymongo import MongoClient

TEST_MONGO_URI = 'mongodb://localhost/test'
TEST_DB_NAME = 'test'

@pytest.fixture
def collection():
    mongo = MongoClient(TEST_MONGO_URI)
    db = mongo[TEST_DB_NAME]
    collection = db.dates

    yield collection

    mongo.drop_database('test')

@pytest.fixture
def client(collection):
    from app import create_app
    app = create_app()

    app.config.update({
        "MONGO_CONNECTION": TEST_MONGO_URI,
        "MONGO_DB": TEST_DB_NAME,
        "TESTING": True,
    })

    test_client = Client(app)

    yield test_client
