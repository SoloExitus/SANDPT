import unittest
from Task1 import is_palindrome


class TestPalindromeCase(unittest.TestCase):
    def test_palidrome1(self):
        self.assertEqual(is_palindrome("A man, a plan, a canal -- Panama"), True, "Should be True")

    def test_palidrome2(self):
        self.assertEqual(is_palindrome("Madam, I'm Adam!"), True, "Should be True")

    def test_number(self):
        self.assertEqual(is_palindrome(333), False, "Should be False")

    def test_None(self):
        self.assertEqual(is_palindrome(None), False, "Should be False")

    def test_Abracadabra(self):
        self.assertEqual(is_palindrome("Abracadabra"), False, "Should be False")

if __name__ == '__main__':
    unittest.main()
