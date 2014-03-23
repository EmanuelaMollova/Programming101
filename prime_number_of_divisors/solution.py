# Solution 1
def prime_number_of_divisors(n):
    return is_prime(len(find_divisors(n)))


def is_prime(n):
    if n > 1 and not(list(filter(lambda i: n % i == 0, range(2, n)))):
        return True
    else:
        return False


def find_divisors(n):
    return list(filter(lambda number: n % number == 0, range(1, n + 1)))

# Solution 2
# def prime_number_of_divisors(n):
#     number = 0
#     for divisor in range(1, n + 1):
#         if n % divisor == 0:
#             number += 1

#     return number
