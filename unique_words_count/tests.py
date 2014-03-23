import unittest
from solution import unique_words_count


class UniqueWordsCountTest(unittest.TestCase):
    def test_unique_words_count(self):
        self.assertEqual(3, unique_words_count(["apple", "banana", "apple", "pie"]))
        self.assertEqual(2, unique_words_count(["python", "python", "python", "ruby"]))
        self.assertEqual(1, unique_words_count(["HELLO!"] * 10))
        self.assertEqual(0, unique_words_count([]))

if __name__ == '__main__':
    unittest.main()
