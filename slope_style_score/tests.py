import unittest
from solution import slope_style_score


class SlopeStyleScoreTest(unittest.TestCase):
    def test_slope_style_score(self):
        self.assertEqual(94.66, slope_style_score([94, 95, 95, 95, 90]))
        self.assertEqual(80.0, slope_style_score([60, 70, 80, 90, 100]))
        self.assertEqual(93.5, slope_style_score([96, 95.5, 93, 89, 92]))

if __name__ == '__main__':
    unittest.main()
