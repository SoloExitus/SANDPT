import unittest
from Task4 import sort_list

class TestSortListCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(sort_list([]), [])

    def test_default1(self):
        self.assertEqual(sort_list([2, 4, 6, 8]), [8, 4, 6, 2, 2])

    def test_one(self):
        self.assertEqual(sort_list([1]), [1, 1])

    def test_default2(self):
        self.assertEqual(sort_list([1, 2, 1, 3]), [3, 2, 3, 1, 1])

if __name__ == '__main__':
    unittest.main()
