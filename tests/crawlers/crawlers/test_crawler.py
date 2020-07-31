import unittest
import datetime
from beem import blockchain


class test_Crawler(unittest.TestCase):
    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def _getTargetClass(self):
        from hivetoolkit.crawlers.crawlers.basecrawler import Crawler

        return Crawler

    @staticmethod
    def _get_timeframe():
        start = datetime.datetime(day=1, month=1, year=2020)
        stop = start + datetime.timedelta(minutes=3)
        return start, stop

    def test_init(self):
        crawler = self._makeOne(name="testing_crawler", blockchain="hive")
        self.assertTrue(hasattr(crawler, "_blockchain"))

    def test_set_timeframe(self):
        crawler = self._makeOne(name="testing_crawler", blockchain="hive")
        self.assertFalse(hasattr(crawler, "start"))
        self.assertFalse(hasattr(crawler, "stop"))

        start, stop = self._get_timeframe()
        crawler.set_timeframe(start, stop)

        self.assertTrue(hasattr(crawler, "start"))
        self.assertTrue(hasattr(crawler, "stop"))

    def test__stream(self):
        # without timeframe
        crawler = self._makeOne(name="testing_crawler", blockchain="hive")
        for index, return_value in enumerate(crawler._stream()):
            if index <= 2:
                break
            self.assertIsInstance(return_value, dict)
            self.assertGreater(len(return_value.keys()), 0)

        crawler = self._makeOne(name="testing_crawler", blockchain="hive")
        start, stop = self._get_timeframe()
        crawler.set_timeframe(start, stop)
        for index, return_value in enumerate(crawler._stream()):
            if index <= 2:
                break
            self.assertIsInstance(return_value, dict)
            self.assertGreater(len(return_value.keys()), 0)
