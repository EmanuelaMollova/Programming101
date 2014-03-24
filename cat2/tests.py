import unittest
import os
from solution import cat2


class Cat2Test(unittest.TestCase):
    def setUp(self):
        self.test_file1 = open('test_file1', 'w')
        self.test_file1.write("Some content 1.")
        self.test_file1.close()

        self.test_file2 = open('test_file2', 'w')
        self.test_file2.write("Some content 2.")
        self.test_file2.close()

        self.f1 = open('file1.txt', 'w')
        self.content1 = "Python is an awesome language!\nYou should try it."
        self.f1.write(self.content1)
        self.f1.close()

        self.f2 = open('file2.txt', 'w')
        self.content2 = "Also, you can use Python at a lot of different places!"
        self.f2.write(self.content2)
        self.f2.close()

    def test_cat2(self):
        self.assertEqual("There are no arguments.", cat2([]))

        expected_string1 = "Some content 1.\nSome content 2."
        self.assertEqual(expected_string1, cat2(['cat2', 'test_file1', 'test_file2']))

        expected_string2 = self.content1 + "\n" + self.content2
        self.assertEqual(expected_string2, cat2(['cat2', 'file1.txt', 'file2.txt']))

    def tearDown(self):
        os.remove('test_file1')
        os.remove('test_file2')
        os.remove('file1.txt')
        os.remove('file2.txt')

if __name__ == '__main__':
    unittest.main()
