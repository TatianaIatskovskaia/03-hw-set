from main import max_negative_repr
from unittest import TestCase, main

class TestMaxNegativeRepr(TestCase):

    def test_not_exist_positive_negative_pair(self):
        self.assertEqual(max_negative_repr([1, 2, 3, 4]), -1)
        self.assertEqual(max_negative_repr([-1, -2, -3, -4]), -1)
        self.assertEqual(max_negative_repr([0]), -1)
        self.assertEqual(max_negative_repr([]), -1)

    def test_exist_positive_negative_pair(self):
        self.assertEqual(max_negative_repr([100, 4, 1, 1, 4, 100, -1]), 1)
        self.assertEqual(max_negative_repr([-5, 7, 5, 13, -10, 21, 10]), 10)
        self.assertEqual(max_negative_repr([100, 4, 1, -1, -4, -100]), 100)
        self.assertEqual(max_negative_repr([1, 0, 3, 4, -1, -0]), 1)

