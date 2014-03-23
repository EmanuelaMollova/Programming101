import unittest
from solution import goldbach


class GoldbachTest(unittest.TestCase):
    def test_goldbach(self):
        self.assertEqual([(2, 2)], goldbach(4))
        self.assertEqual([(3, 3)], goldbach(6))
        self.assertEqual([(3, 5)], goldbach(8))
        self.assertEqual([(3, 7), (5, 5)], goldbach(10))
        self.assertEqual([(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)], goldbach(100))

if __name__ == '__main__':
    unittest.main()
