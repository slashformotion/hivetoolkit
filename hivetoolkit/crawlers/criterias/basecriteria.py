import datetime
from ...utils import arguments


class BaseCriteria:
    def __init__(self):
        pass

    def setTimeframe(self, start, stop):
        if isinstance(start, datetime.datetime):
            self.start = start
        else:
            raise TypeError("start argument must be an instance of datetime.datetime")

        if isinstance(stop, datetime.datetime):
            self.stop = stop
        else:
            raise TypeError("stop argument must be an instance of datetime.datetime")

        if start >= stop:
            raise RuntimeError("stop({}) < start({})".format(stop, start))


class ConfigHandler:
    pass
