import unittest
from solution import count_consonants


class CountConsonantsTest(unittest.TestCase):
    def test_count_consonants(self):
        self.assertEqual(4, count_consonants("Python"))
        self.assertEqual(11, count_consonants("Theistareykjarbunga"))
        self.assertEqual(7, count_consonants("grrrrgh!"))
        self.assertEqual(44, count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
        self.assertEqual(6, count_consonants("A nice day to code!"))

if __name__ == '__main__':
    unittest.main()
