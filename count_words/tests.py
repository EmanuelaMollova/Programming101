import unittest
from solution import count_words


class CountWordsTest(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual({'apple': 2, 'pie': 1, 'banana': 1}, count_words(["apple", "banana", "apple", "pie"]))
        self.assertEqual({'ruby': 1, 'python': 3}, count_words(["python", "python", "python", "ruby"]))
        self.assertEqual({'hackbg': 2}, count_words(["hackbg", "hackbg"]))

if __name__ == '__main__':
    unittest.main()
