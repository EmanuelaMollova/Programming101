def sum_of_divisors(n):
    return sum(find_divisors(n))


def find_divisors(n):
    return list(filter(lambda number: n % number == 0, range(1, n + 1)))
