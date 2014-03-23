# Solution 1
def number_to_list(n):
    return list(map(int, str(n)))


# Solution 2
# def number_to_list_helper(n):
#     if n < 10:
#         return [n]

#     return [n % 10] + number_to_list_helper(n // 10)


# def number_to_list(n):
#     return number_to_list_helper(n)[::-1]
