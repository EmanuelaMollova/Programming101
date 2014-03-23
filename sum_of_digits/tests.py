import unittest
from solution import sum_of_digits


class SumOfDigitsTest(unittest.TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(43, sum_of_digits(1325132435356))
        self.assertEqual(1 + 2 + 3, sum_of_digits(123))
        self.assertEqual(6, sum_of_digits(6))
        self.assertEqual(1, sum_of_digits(-10))
        self.assertEqual(0, sum_of_digits(0))
        self.assertEqual(4 + 3 + 5, sum_of_digits(400003005))

if __name__ == '__main__':
    unittest.main()
