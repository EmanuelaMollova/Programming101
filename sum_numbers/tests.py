import unittest
import os
from solution import sum_numbers


class SumNumbersTest(unittest.TestCase):
    def setUp(self):
        self.test_file = open('test_file', 'w')
        self.test_file.write("1 2 3 4 5")
        self.test_file.close()

        self.f = open('file.txt', 'w')
        self.f.write("0")
        self.f.close()

    def test_sum_numbers(self):
        self.assertEqual("Please give a filename.", sum_numbers([]))
        self.assertEqual(15, sum_numbers(['sum_numbers', 'test_file']))
        self.assertEqual(0, sum_numbers(['sum_numbers', 'file.txt']))

    def tearDown(self):
        os.remove('test_file')
        os.remove('file.txt')

if __name__ == '__main__':
    unittest.main()
