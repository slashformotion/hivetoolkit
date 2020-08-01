from hivetoolkit.utils.utils import intersection
import unittest


class test_intersection(unittest.TestCase):
    def _exe(self, *args, **kwargs):
        return self._get_obj()(*args, **kwargs)

    def _get_obj(self):
        from hivetoolkit.utils import intersection

        return intersection

    def test_intersection(self):
        lst1 = ["devtalk"]
        lst2 = ["dev", "flask", "devtalk", "blog", "tech"]

        self.assertListEqual(self._exe(lst1, lst2), ["devtalk"])
