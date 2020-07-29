import datetime
from unittest import TestCase
from hivetoolkit.crawlers.criterias import CommentCriteria


class test_CommentCriteria(TestCase):

    def setUp(self):
        self.criteria_fixture = CommentCriteria()
    
    def tearDown(self):
        del self.criteria_fixture

    def test_setTimeFrame(self):
        start = datetime.datetime(day=1, month=1, year=2020)
        stop = start + datetime.timedelta(hours=1)
        self.criteria_fixture.setTimeframe(start, stop)
        
        self.assertTrue(
            hasattr(
                self.criteria_fixture,
                "start"
            )
        )

        self.assertTrue(
            hasattr(
                self.criteria_fixture,
                "start"
            )
        )

