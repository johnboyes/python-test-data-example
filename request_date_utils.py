from datetime import datetime
from datetime import timedelta


def request_date(format="{:%Y-%m-%d %H:%M}", days=0):
    return format.format(datetime.now() + timedelta(days=days))
