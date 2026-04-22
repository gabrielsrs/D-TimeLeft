from flask_restx import reqparse
class TZFilterParser:
    """Fields to validate timezone filter"""
    def __init__(self):
        """Initiate parser"""
        self.create_parser = reqparse.RequestParser(bundle_errors=True, trim=True)

    def __call__(self):
        """
        Add fields in parser

        :return: A RequestParser object with created config
        """
        self.create_parser.add_argument('timezone', required=False, type=str, location='args')
        self.create_parser.add_argument('offset', required=False, type=str, location='args')

        return self.create_parser
