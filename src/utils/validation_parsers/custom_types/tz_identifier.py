from zoneinfo import available_timezones

def tz_identifier(value):
    if value not in available_timezones():
        raise ValueError({"code": 400, "message": f'Invalid tz identifier "{value}"'})
    return value

tz_identifier.__schema__ = {"type": "string", "format": "tz identifier"}
