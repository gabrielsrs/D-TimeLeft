from flask import Flask
from src.api import api
from src.utils.error_handler import ErrorHandler

def create_app():
    from dotenv import load_dotenv
    import os
    load_dotenv()

    app = Flask(__name__)
    app.config.from_pyfile('.env')

    api.init_app(app)

    app.register_error_handler(Exception, lambda error: ErrorHandler(error)())

    return app
