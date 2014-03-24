import unittest
import os
from solution import cat


class CatTest(unittest.TestCase):
    def setUp(self):
        self.test_file = open('test_file', 'w')
        self.test_file.write("Some content.")
        self.test_file.close()

        self.f = open('file.txt', 'w')
        self.content = "This is some file\nAnd cat is printing it's contents"
        self.f.write(self.content)
        self.f.close()

    def test_cat_helper(self):
        self.assertEqual( "There is more than one file or no arguments.", cat([]))
        self.assertEqual("Some content.", cat(['cat', 'test_file']))
        self.assertEqual(self.content, cat(['cat', 'file.txt']))

    def tearDown(self):
        os.remove('test_file')
        os.remove('file.txt')

if __name__ == '__main__':
    unittest.main()
