from flask_restx import Resource, Namespace
from ..handlers.timezones_handler import TimezonesHandler
from ..utils.validation_parsers.tz_filter import TZFilterParser
from src.utils.response_marshalling.timezones_marchalling import timezones_models, timezones

api = Namespace('Timezones', description='timezones route')

def assign_models(model):
    api.models[model.name] = model

for models in timezones_models:
    assign_models(models)

@api.route('')
class Timezones(Resource):
    """
        Resource for managing timezones.

        Operations:
        - **Read** (`GET /timezones`) → Retrieve timezones.
            :return: A json with contain the timezones, with offset and identifiers
    """
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

        self.tz_filter = TZFilterParser()

    def _tz_filter(self): # pragma: no cover
        """Get parser related with filter"""
        return self.tz_filter()

    @api.marshal_with(timezones)
    @api.expect(_tz_filter)
    def get(self):
        """Get all available timezones."""
        timezones_handler = TimezonesHandler()
        args = self.tz_filter().parse_args()
        return timezones_handler.timezones(args)
