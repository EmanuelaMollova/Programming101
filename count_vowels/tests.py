import unittest
from solution import count_vowels


class CountVowelsTest(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(2, count_vowels("Python"))
        self.assertEqual(8, count_vowels("Theistareykjarbunga"))
        self.assertEqual(0, count_vowels("grrrrgh!"))
        self.assertEqual(22, count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
        self.assertEqual(8, count_vowels("A nice day to code!"))

if __name__ == '__main__':
    unittest.main()
