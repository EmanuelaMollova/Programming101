import unittest
from solution import simplify_fraction


class SimplifyFractionTest(unittest.TestCase):
    def test_simplify_fraction(self):
        self.assertEqual((1, 3), simplify_fraction((3, 9)))
        self.assertEqual((1, 7), simplify_fraction((1, 7)))
        self.assertEqual((2, 5), simplify_fraction((4, 10)))
        self.assertEqual((3, 22), simplify_fraction((63, 462)))

if __name__ == '__main__':
    unittest.main()
