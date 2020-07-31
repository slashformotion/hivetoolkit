import unittest

from beem import blockchain


class test_Crawler(unittest.TestCase):
    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def _getTargetClass(self):
        from hivetoolkit.crawlers.crawlers.basecrawler import Crawler

        return Crawler

    def test_init(self):
        crawler = self._makeOne(name="testing_basecrawler", blockchain="hive")
        self.assertTrue(hasattr(crawler, "_blockchain"))
