import unittest

__author__ = 'joeny'


class BaseUnitTest(unittest.TestCase):

    def assertTolerance(self, value1, value2, percent=0.01):
        if value1 is None:
            # self.assertRaises(Exception)
            raise Exception('None value')

        if isinstance(value1, list):
            for x, y in zip(value1, value2):
                self._assertTolerance(x, y, percent)

        else:
            self._assertTolerance(value1, value2, percent)

    def difference(self, value1, value2):
        return abs(value1 - value2)

    def _assertTolerance(self, value1, value2, percent):
        if isinstance(value1, str) or isinstance(value2, str):
            self.assertEqual(value1, value2)

            return

        try:
            ratio = abs(value1 - value2)/abs(value2)

            self.assertLess(ratio, percent)
        except ZeroDivisionError as e:
            self.assertLess(self.difference(value1, value2), percent)
