import unittest


class testbase_Criteria(unittest.TestCase):
    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def _getTargetClass(self):
        from hivetoolkit.crawlers.criterias.basecriteria import BaseCriteria

        return BaseCriteria

    def test_set_rule(self):
        criteria = self._makeOne()

        self.assertTrue(criteria.rules == {})

        dummy_value = ["user1", "user2"]
        criteria.set_rule("empty_rule", dummy_value)

        self.assertFalse(criteria.rules == {})

        self.assertTrue(criteria.rules == {"empty_rule": dummy_value})

        with self.assertRaises(NotImplementedError):
            criteria.set_rule("not_a_valid_rule_name", {})

        criteria = self._makeOne()

        with self.assertRaises(TypeError):
            criteria.set_rule("empty_rule", "not a valid type")

    def test_reset(self):
        criteria = self._makeOne()
        dummy_value = ["user1", "user2"]

        criteria.set_rule("empty_rule", dummy_value)

        self.assertTrue(criteria.rules == {"empty_rule": dummy_value})

        criteria.reset()

        self.assertFalse(criteria.rules == {"empty_rule": dummy_value})
        self.assertTrue(criteria.rules == {})
