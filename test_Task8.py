import unittest
from Task8 import multiply_numbers

class TestMultiplyNumbersCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(multiply_numbers(), None)

    def test_char(self):
        self.assertEqual(multiply_numbers('ss'), None)

    def test_number(self):
        self.assertEqual(multiply_numbers('1234'), 24)

    def test_charAndNumbers(self):
        self.assertEqual(multiply_numbers('sssdd34'), 12)

    def test_float(self):
        self.assertEqual(multiply_numbers(2.3), 6)

    def test_list(self):
        self.assertEqual(multiply_numbers([5, 6, 4]), 120)


if __name__ == '__main__':
    unittest.main()
