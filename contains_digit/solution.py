# Solution 1
def contains_digit(number, digit):
    return False if str(number).find(str(digit)) == -1 else True


# Solution 2
# def contains_digit(number, digit):
#     if number < 10:
#         return number == digit

#     return number % 10 == digit or contains_digit(number // 10, digit)
