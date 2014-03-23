# Solution 1
def is_increasing(seq):
    return all(x < y for x, y in zip(seq, seq[1:]))


# Solution 2
# def is_increasing(seq):
#     for i in range(0, len(seq) - 1):
#         if seq[i] >= seq[i+1]:
#             return False

#     return True
