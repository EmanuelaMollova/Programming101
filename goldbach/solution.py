def goldbach(n):
    primes = []
    for i in range(2, n // 2 + 1):
        if is_prime(i):
            primes.append(i)

    result = []
    for prime in primes:
        if is_prime(n - prime):
            result.append((prime, n - prime))

    return result


def is_prime(n):
    if n > 1 and not(list(filter(lambda i: n % i == 0, range(2, n)))):
        return True
    else:
        return False
