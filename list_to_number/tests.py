import unittest
from solution import list_to_number


class ListToNumberTest(unittest.TestCase):
    def test_list_to_number(self):
        self.assertEqual(123, list_to_number([1, 2, 3]))
        self.assertEqual(99999, list_to_number([9, 9, 9, 9, 9]))
        self.assertEqual(123023, list_to_number([1, 2, 3, 0, 2, 3]))
        self.assertEqual(0, list_to_number([0]))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
