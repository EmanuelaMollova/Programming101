import unittest
from solution import prime_number_of_divisors

class PrimeNumberOfDivisorsTest(unittest.TestCase):
    def test_prime_number_of_divisors(self):
        self.assertTrue(prime_number_of_divisors(7))
        self.assertTrue(not prime_number_of_divisors(8))
        self.assertTrue(prime_number_of_divisors(9))
        self.assertTrue(not prime_number_of_divisors(1))
        self.assertTrue(prime_number_of_divisors(2))

if __name__ == '__main__':
    unittest.main()
