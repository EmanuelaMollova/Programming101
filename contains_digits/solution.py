# Solution 1
def contains_digits(number, digits):
    contained = list(filter(lambda x: contains_digit(number, x), digits))
    return len(digits) == len(contained)


def contains_digit(number, digit):
    return False if str(number).find(str(digit)) == -1 else True


# Solution 2
# def contains_digits(number, digits):
#     if not digits:
#         return True

#     for item in digits:
#         if not(contains_digit(number, item)):
#             return False

#     return True
