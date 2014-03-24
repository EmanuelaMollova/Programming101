import unittest
import os
from solution import generate_numbers


class GenerateNumbersTest(unittest.TestCase):
    def setUp(self):
        self.test_file = open('test_file', 'w+')

    def test_cat_helper(self):
        self.assertEqual("Please give a filename and a number.", generate_numbers([]))

        content = generate_numbers(['generate_numbers', 'test_file', 5])
        self.assertEqual(5, len(content.split(" ")))
        file_content = self.test_file.read()
        self.assertEqual(content, file_content)

        self.test_file.close()
    def tearDown(self):
        os.remove('test_file')

if __name__ == '__main__':
    unittest.main()
