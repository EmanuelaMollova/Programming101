import unittest
from solution import sum_of_min_and_max


class SumOfMinAndMaxTest(unittest.TestCase):
    def test_sum_of_min_and_max(self):
        self.assertEqual(10, sum_of_min_and_max([1, 2, 3, 4, 5, 6, 8, 9]))
        self.assertEqual(90, sum_of_min_and_max([-10, 5, 10, 100]))
        self.assertEqual(2, sum_of_min_and_max([1]))
        self.assertEqual(0, sum_of_min_and_max([0]))
        self.assertEqual(0, sum_of_min_and_max([-5, 2, 3, 5]))

if __name__ == '__main__':
    unittest.main()
