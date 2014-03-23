# Solution 1
from collections import defaultdict


def groupby(func, seq):
    result = defaultdict(list)
    for item in seq:
        result[func(item)].append(item)

    return result


# Solution 2
# def groupby(func, seq):
#     hash = {}
#     for item in seq:
#         result = func(item)
#         if result not in hash:
#             hash[result] = [item]
#         else:
#             hash[result].append(item)

#     return hash
