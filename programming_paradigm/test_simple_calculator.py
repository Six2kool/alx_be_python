import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        # This runs before EVERY test — makes a fresh calculator
        self.calc = SimpleCalculator()

    # TEST 1: Addition
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-5, 7), 2)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    # TEST 2: Subtraction
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 8), -8)
        self.assertEqual(self.calc.subtract(-3, -3), 0)
        self.assertEqual(self.calc.subtract(100, -50), 150)

    # TEST 3: Multiplication
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-4, 3), -12)
        self.assertEqual(self.calc.multiply(-5, -5), 25)

    # TEST 4: Division (normal cases)
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(0, 5), 0.0)

    # TEST 5: Division by zero (SUPER IMPORTANT!)
    def test_division_by_zero(self):
        self.assertEqual(self.calc.divide(10, 0), None)
        self.assertEqual(self.calc.divide(-5, 0), None)
        self.assertIsNone(self.calc.divide(0, 0))  # extra cool way to check None

# This line runs all the tests when you run the file
if __name__ == '__main__':
    unittest.main()