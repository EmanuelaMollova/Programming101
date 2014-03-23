def prime_factorization(n):
    tuples = []
    prime_divisors = list(filter(is_prime, find_divisors(n)))

    for prime in prime_divisors:
        count = 0
        while n % prime == 0:
            count += 1
            n = n / prime
        tuples.append((prime, count))

    return tuples


def find_divisors(n):
    return list(filter(lambda number: n % number == 0, range(1, n + 1)))


def is_prime(n):
    if n > 1 and not(list(filter(lambda i: n % i == 0, range(2, n)))):
        return True
    else:
        return False
