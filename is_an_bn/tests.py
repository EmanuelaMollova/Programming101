import unittest
from solution import is_an_bn


class IsAnBnTest(unittest.TestCase):
    def test_is_an_bn(self):
        self.assertTrue(is_an_bn(""))
        self.assertTrue(not is_an_bn("rado"))
        # self.assertTrue(not is_an_bn("aaabb"))
        # self.assertTrue(is_an_bn("aaabbb"))
        # self.assertTrue(not is_an_bn("aabbaabb"))
        # self.assertTrue(not is_an_bn("bbbaaa"))
        # self.assertTrue(is_an_bn("aaaaabbbbb"))

if __name__ == '__main__':
    unittest.main()
