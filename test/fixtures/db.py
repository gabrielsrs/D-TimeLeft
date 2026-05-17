import pytest
from werkzeug.test import Client
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

@pytest.fixture
def collection():
    mongo = MongoClient(os.getenv("TEST_MONGO_URI"))
    db = mongo[os.getenv("TEST_DB_NAME")]
    collection = db.dates

    yield collection

    mongo.drop_database('test')

@pytest.fixture
def client(collection):
    from app import create_app
    app = create_app()

    app.config["MONGO_URI"] = os.getenv("TEST_MONGO_URI")
    app.config["MONGO_DB"] = os.getenv("TEST_DB_NAME")

    test_client = Client(app)

    yield test_client
