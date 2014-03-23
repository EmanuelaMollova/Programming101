import unittest
from solution import contains_digit


class ContainsDigitTest(unittest.TestCase):
    def test_contains_digit(self):
        self.assertTrue(not contains_digit(123, 4))
        self.assertTrue(contains_digit(42, 2))
        self.assertTrue(contains_digit(1000, 0))
        self.assertTrue(not contains_digit(12346789, 5))

if __name__ == '__main__':
    unittest.main()
