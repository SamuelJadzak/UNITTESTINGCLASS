import unittest
from Calculator import calculator

class testcase1(unittest.TestCase):
    def test_additioncheck(self):
        result = calculator.add(5,5)
        self.assertEqual(result, 10)
    def test_subtractioncheck(self):
        result = calculator.subtract(10,5)
        self.assertEqual(result, 5)
    def test_multiplycheck(self):
        result = calculator.multiply(2,2)
        self.assertEqual(result, 4)
    def test_dividecheck(self):
        result = calculator.divide(4,2)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()