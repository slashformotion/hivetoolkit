from unittest import TestCase
from tests.utils import SuperFixture
from .testbases_criterias import testbase_Criteria


class testbase_CommentCriteria(testbase_Criteria):
    def _getTargetClass(self):
        from hivetoolkit.crawlers.criterias import CommentCriteria

        return CommentCriteria

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)


class test_setTimeFrame(testbase_CommentCriteria):
    def test_setTimeFrame_intendedBehavior(self):
        start, stop = self._getStandartStartStop()

        criteria = self._makeOne()

        # attr should not exists
        self.assertFalse(hasattr(criteria, "start"))
        self.assertFalse(hasattr(criteria, "start"))

        criteria.setTimeframe(start, stop)

        # attr should exists
        self.assertTrue(hasattr(criteria, "start"))
        self.assertTrue(hasattr(criteria, "start"))

    def test_setTimeFrame_swapArguments(self):
        criteria = self._makeOne()

        # swap of start and stop
        stop, start = self._getStandartStartStop()

        with self.assertRaises(RuntimeError):
            criteria.setTimeframe(start, stop)


class test_setAllowedAtuthors(testbase_CommentCriteria):
    def test_setAllowedAtuthors_intendedBehavior(self):
        authors = ["1", "sdfjklsdnf"]

        criteria = self._makeOne()

        self.assertFalse(hasattr(criteria, "allowed_authors"))

        criteria.setAllowedAuthors(authors)

        self.assertTrue(hasattr(criteria, "allowed_authors"))


class test_setUnallowedAtuthors(testbase_CommentCriteria):
    def test_setUnallowedAtuthors_intendedBehavior(self):
        authors = ["1", "sdfjklsdnf"]

        criteria = self._makeOne()

        self.assertFalse(hasattr(criteria, "unallowed_authors"))

        criteria.setUnallowedAuthors(authors)

        self.assertTrue(hasattr(criteria, "unallowed_authors"))


class test_setAllowedTags(testbase_CommentCriteria):
    def test_setAllowedTags_intendedBehavior(self):
        tags = ["1", "sdfjklsdnf"]
        attr = "allowed_tags"
        criteria = self._makeOne()

        self.assertFalse(hasattr(criteria, attr))

        criteria.setAllowedTags(tags)

        self.assertTrue(hasattr(criteria, attr))

class test_setUnallowedTags(testbase_CommentCriteria):
    def test_setUnallowedTags_intendedBehavior(self):
        tags = ["1", "sdfjklsdnf"]
        attr = "unallowed_tags"
        criteria = self._makeOne()

        self.assertFalse(hasattr(criteria, attr))

        criteria.setUnallowedTags(tags)

        self.assertTrue(hasattr(criteria, attr))