import unittest
from solution import is_int_palindrome


class IsIntPalindromeTest(unittest.TestCase):
    def test_is_int_palindrome(self):
        self.assertTrue(is_int_palindrome(1))
        self.assertTrue(not is_int_palindrome(42))
        self.assertTrue(is_int_palindrome(100001))
        self.assertTrue(is_int_palindrome(999))
        self.assertTrue(not is_int_palindrome(123))
        self.assertTrue(is_int_palindrome(12344321))

if __name__ == '__main__':
    unittest.main()
