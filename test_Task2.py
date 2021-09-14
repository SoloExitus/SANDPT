import unittest
from Task2 import coincidence

class TestcoincidenceCase(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(coincidence([1, 2, 3, 4, 5], range(3, 6)), [3, 4, 5], "Not correct")

    def test_withoutArgs(self):
        self.assertEqual(coincidence(), [], "Not correct")

    def test_withDiffrentValues(self):
        self.assertEqual(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)), [1, 2, 2.5], "Not correct")



if __name__ == '__main__':
    unittest.main()
