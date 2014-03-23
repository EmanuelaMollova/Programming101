import unittest
from solution import number_to_list


class NumberToListTest(unittest.TestCase):
    def test_number_to_list(self):
        self.assertEqual([1, 2, 3], number_to_list(123))
        self.assertEqual([9, 9, 9, 9, 9], number_to_list(99999))
        self.assertEqual([1, 2, 3, 0, 2, 3], number_to_list(123023))
        self.assertEqual([0], number_to_list(0))

if __name__ == '__main__':
    unittest.main()
