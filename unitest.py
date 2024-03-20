import unittest
from show_tasks_module import plus, minus, mul, division, div, remainder, div_by_degree


class TestCalcFunctions(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(plus(3, 4), 7)

    def test_minus(self):
        self.assertEqual(minus(10, 5), 5)

    def test_mul(self):
        self.assertEqual(mul(5, 2), 10)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)

    def test_div(self):
        self.assertEqual(div(10, 3), 3)

    def test_remainder(self):
        self.assertEqual(remainder(10, 3), 1)

    def test_div_by_degree(self):
        self.assertEqual(div_by_degree(2, 3), 8)
