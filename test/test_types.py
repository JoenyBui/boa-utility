from unittest import TestCase

from boautil.types import convert_to_float, convert_to_int


class Model(object):

    def __init__(self, *args, **kwargs):
        self.keys = kwargs.get('keys', {})

    @property
    def I1(self):
        return self.keys.get('I1')

    @I1.setter
    @convert_to_int
    def I1(self, value):
        self.keys['I1'] = value

    @property
    def F1(self):
        return self.keys.get('F1')

    @F1.setter
    @convert_to_float
    def F1(self, value):
        self.keys['F1'] = value


class TestTypes(TestCase):

    def setUp(self):
        self.m1 = Model()

    def test_int(self):
        self.m1.I1 = 10.0
        self.assertEqual(self.m1.I1, 10.0)
        self.assertTrue(isinstance(self.m1.I1, int))

        self.m1.I1 = None
        self.assertEqual(self.m1.I1, None)

        self.m1.I1 = ""
        self.assertEqual(self.m1.I1, None)

        self.m1.I1 = "10.0"
        self.assertEqual(self.m1.I1, None)

        self.m1.I1 = "10"
        self.assertEqual(self.m1.I1, 10)
        self.assertTrue(isinstance(self.m1.I1, int))

        self.m1.I1 = (10.0, None, "", "10.0")
        self.assertEqual(self.m1.I1, (10, None, None, None))
        self.assertTrue(isinstance(self.m1.I1, tuple))

        self.m1.I1 = [10.5, None, "", "10.0"]
        self.assertEqual(self.m1.I1, [10, None, None, None])
        self.assertTrue(isinstance(self.m1.I1, list))

    def test_float(self):
        self.m1.F1 = 10.0
        self.assertEqual(self.m1.F1, 10.0)

        self.m1.F1 = None
        self.assertEqual(self.m1.F1, None)

        self.m1.F1 = ""
        self.assertEqual(self.m1.F1, None)

        self.m1.F1 = "10.0"
        self.assertEqual(self.m1.F1, 10.0)

        self.m1.F1 = (10.0, None, "", "10.0")
        self.assertEqual(self.m1.F1, (10.0, None, None, 10.0))
        self.assertTrue(isinstance(self.m1.F1, tuple))

        self.m1.F1 = [10.0, None, "", "10.0"]
        self.assertEqual(self.m1.F1, [10.0, None, None, 10.0])
        self.assertTrue(isinstance(self.m1.F1, list))
