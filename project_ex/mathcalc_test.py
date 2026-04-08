from mathcalc import add
import unittest

class TestDiscountCalculator(unittest.TestCase):
    def test_positive(self):
        result = add(10,10)
        self.assertEqual(result, 20)
    def test_negative(self):
        result = add(-10,-10)
        self.assertEqual(result, -20)

unittest.main()
