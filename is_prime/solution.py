# Solution 1
def is_prime(n):
    if n > 1 and not(list(filter(lambda i: n % i == 0, range(2, n)))):
        return True
    else:
        return False


# Solution 2
# def is_prime(n):
#     if n <= 1:
#         return False

#     for divisor in range(2, n):
#         if n % divisor == 0:
#             return False

#     return True
