import unittest
from Task3 import max_odd

class TestmaxOddCase(unittest.TestCase):
    def test_default(self):
        self.assertEqual(max_odd([1, 2, 3, 4, 4]), 3)

    def test_withFloat(self):
        self.assertEqual(max_odd([21.0, 2, 3, 4, 4]), 21)

    def test_withAnyTypes(self):
        self.assertEqual(max_odd(['ololo', 2, 3, 4, [1, 2], None]), 3)

    def test_withStrings(self):
        self.assertEqual(max_odd(['ololo', 'fufufu']), None)

    def test_withStrings(self):
        self.assertEqual(max_odd([2, 2, 4]), None)

if __name__ == '__main__':
    unittest.main()
