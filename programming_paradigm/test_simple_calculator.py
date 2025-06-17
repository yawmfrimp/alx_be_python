import unittest
from simple_calculator import SimpleCalculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def testadd(self):
        self.assertEqual(self.calc.add(3,2), 5)
        self.assertEqual(self.calc.add(-10,-2), -12)
        self.assertEqual(self.calc.add(-8,2), -6)

    def testsubtract(self):
        self.assertEqual(self.calc.subtract(10,2), 8)
        self.assertEqual(self.calc.subtract(3,5), -2)

    def testmultiply(self):
        self.assertEqual(self.calc.multiply(3,2), 6)
        self.assertEqual(self.calc.multiply(11,-11), -121)
        self.assertEqual(self.calc.multiply(-6,-3), 18)

    def testdivide(self):
        self.assertEqual(self.calc.divide(16,-2), -8)
        self.assertEqual(self.calc.divide(3,2), 1.5)
        self.assertEqual(self.calc.divide(-24,-6), 4)
        self.assertEqual(self.calc.divide(14,0), None)
        

unittest.main(verbosity=2)