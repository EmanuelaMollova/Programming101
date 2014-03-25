import unittest
import os
from solution import wc


class WcTest(unittest.TestCase):
    def setUp(self):
        self.test_file = open('test_file', 'w')

        content = [
            "This is a test file.",
            "With some word.",
            "And some line."
        ]

        content = "\n".join(content)

        self.test_file.write(content)
        self.test_file.close()

        self.f = open('file.txt', 'w')
        self.content = ""
        self.f.write(self.content)
        self.f.close()

    def test_wc_works_without_parameters(self):
        self.assertEqual("Please give a command and a filename.", wc([]))

    def test_wc_works_for_words(self):
        self.assertEqual(11, wc(['wc', 'words', 'test_file']))
        self.assertEqual(0, wc(['wc', 'words', 'file.txt']))

    def test_wc_works_for_lines(self):
        self.assertEqual(3, wc(['wc', 'lines', 'test_file']))
        self.assertEqual(1, wc(['wc', 'lines', 'file.txt']))

    def test_wc_works_for_chars(self):
        self.assertEqual(51, wc(['wc', 'chars', 'test_file']))
        self.assertEqual(0, wc(['wc', 'chars', 'file.txt']))

    def tearDown(self):
        os.remove('test_file')
        os.remove('file.txt')

if __name__ == '__main__':
    unittest.main()
