import unittest
from solution import contains_digits


class ContainsDigitsTest(unittest.TestCase):
    def test_contains_digits(self):
        self.assertTrue(contains_digits(402123, [0, 3, 4]))
        self.assertTrue(not contains_digits(666, [6, 4]))
        self.assertTrue(not contains_digits(123456789, [1, 2, 3, 0]))
        self.assertTrue(contains_digits(456, []))

if __name__ == '__main__':
    unittest.main()
