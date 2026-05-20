from pymongo import MongoClient
from flask import current_app, has_app_context

from dotenv import load_dotenv
import os

def create_conn():
    """Create database connection"""

    if has_app_context():
        client = MongoClient(current_app.config["MONGO_URI"])
        db = client[current_app.config["MONGO_DB"]]
    else:
        load_dotenv()
        client = MongoClient(os.getenv("TEST_MONGO_URI"))
        db = client[(os.getenv("TEST_DB_NAME"))]

    collection = db.dates

    return collection
