import unittest
import os
from solution import cat_helper


class CatTest(unittest.TestCase):
    def setUp(self):
        self.test_file = open('test_file', 'w')
        self.test_file.write("Bla.")
        self.test_file.close()

    def test_cat_helper(self):
        self.assertEqual("There are no arguments", cat_helper([]))
        self.assertEqual("Bla.", cat_helper(['cat', 'test_file']))

    def tearDown(self):
        os.remove('test_file')

if __name__ == '__main__':
    unittest.main()
