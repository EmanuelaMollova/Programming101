import unittest
from solution import nth_fib_lists


class NthFibListsTest(unittest.TestCase):
    def test_nth_fib_lists(self):
        self.assertEqual([1], nth_fib_lists([1], [2], 1))
        self.assertEqual([2], nth_fib_lists([1], [2], 2))
        self.assertEqual([1, 2, 1, 3], nth_fib_lists([1, 2], [1, 3], 3))
        self.assertEqual([1, 2, 3, 1, 2, 3], nth_fib_lists([], [1, 2, 3], 4))
        self.assertEqual([], nth_fib_lists([], [], 100))

if __name__ == '__main__':
    unittest.main()
