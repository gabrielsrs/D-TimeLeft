from zoneinfo import ZoneInfo, available_timezones
import datetime
import tzdata
class TimezonesHandler:
    """Menage get timezones available"""

    def timezones(self, args):
        """
        Get all currents available timezones, and filter by UTC-Offset and Timezone identifiers name

        :param args: The timezone and offset filter/None (dict-like mapping).
        :return: Information from tzdata from each timezone
        """

        timezones = []

        for tz_identifier in available_timezones():
            utc_offset = datetime.datetime.now(ZoneInfo(tz_identifier)).strftime('%z')

            timezones.append({"tz_identifier": tz_identifier, "utc_offset": utc_offset})

        if tz := args.timezone:
            timezones = list(filter(lambda x: tz.lower() in x["tz_identifier"].lower(), timezones))

        if offset := args.offset:
            timezones = list(filter(lambda x: offset in x["utc_offset"], timezones))

        timezones.sort(key=lambda x: x["utc_offset"])

        return {
            "code": 200,
            "message": "tz identifier and utc offset list",
            "tzdb": tzdata.__version__,
            "data": timezones
        }
