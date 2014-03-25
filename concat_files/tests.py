import unittest
import os
from solution import concat_files


class ConcatFilesTest(unittest.TestCase):
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

    def test_concat_files(self):
        self.assertEqual("Please give at least one filename.", concat_files([]))

        expected_string1 = "Some content 1.\n"
        self.assertEqual(expected_string1, concat_files(['concat_files', 'test_file1']))
        megatron = open('MEGATRON', 'r')
        content_megatron = megatron.read()
        megatron.close()
        self.assertEqual(expected_string1, content_megatron)

        expected_string2 = "Some content 2.\nPython is an awesome language!\nYou should try it.\n"
        self.assertEqual(expected_string2, concat_files(['concat_files', 'test_file2', 'file1.txt']))

        megatron = open('MEGATRON', 'r')
        content_megatron = megatron.read()
        megatron.close()
        self.assertEqual("Some content 1.\n" + expected_string2, content_megatron)

    def tearDown(self):
        os.remove('test_file1')
        os.remove('test_file2')
        os.remove('file1.txt')
        os.remove('MEGATRON')

if __name__ == '__main__':
    unittest.main()
