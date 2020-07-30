import datetime
from unittest import TestCase


class testbase_Criteria(TestCase):
    def _getStandartStartStop(self):
        start = datetime.datetime(day=1, month=1, year=2020)
        stop = start + datetime.timedelta(hours=1)

        return start, stop
