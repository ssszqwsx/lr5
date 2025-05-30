import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Add tests for add
    def test_add(self):
        # Arrange
        a, b = 3, 5
        expected = 8

        # Act
        result = self.calc.add(a, b)

        # Assert
        self.assertEqual(result, expected)

    # Test subtract
    def test_subtract(self):
        a, b = 10, 4
        expected = 6
        result = self.calc.subtract(a, b)
        self.assertEqual(result, expected)

    # Test multiply
    def test_multiply(self):
        a, b = 7, 6
        expected = 42
        result = self.calc.multiply(a, b)
        self.assertEqual(result, expected)

    # Test divide
    def test_divide(self):
        a, b = 10, 2
        expected = 5.0
        result = self.calc.divide(a, b)
        self.assertEqual(result, expected)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)

    def test_zero_power_zero(self):
        with self.assertRaises(ValueError):
            self.calc.power(0, 0)

    def test_gcd(self):
        self.assertEqual(self.calc.gcd(48, 18), 6)
        self.assertEqual(self.calc.gcd(-48, 18), 6)

    def test_lcm(self):
        self.assertEqual(self.calc.lcm(4, 5), 20)
        self.assertEqual(self.calc.lcm(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
