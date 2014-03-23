# Solution 1
def list_to_number(digits):
    return int(''.join(map(str, digits)))


# Solution 2
# def list_to_number(digits):
#     max_power = len(digits) - 1
#     number = 0

#     for i in range(0, len(digits)-1):
#         number += digits[i] * (10 ** max_power)
#         max_power -= 1

#     return number + digits[-1]
