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

    app.config["MONGO_URI"] = TEST_MONGO_URI
    app.config["MONGO_DB"] = TEST_DB_NAME

    test_client = Client(app)

    yield test_client
