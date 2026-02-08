from pymongo import MongoClient
from flask import current_app

def create_conn():
    """Create database connection"""
    client = MongoClient(current_app.config["MONGO_URI"])
    db = client[current_app.config["MONGO_DB"]]
    collection = db.dates

    return collection
