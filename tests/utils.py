import datetime
import pathlib


class SuperFixture:
    @property
    def all(self):
        return [
            "string",
            1,
            1.1,
            datetime.datetime.now(),
            datetime.timedelta(hours=1),
            pathlib.Path("."),
            ["voila", 1],
            {"truc": "r"},
        ]  # string, ints, floats, datetime, timedelta

    def getAllBut(self, type_not_allowed):
        for instance in self.all:
            if not isinstance(instance, type_not_allowed):
                yield instance
