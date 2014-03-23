def is_number_balanced(n):
    digits = number_to_list(abs(n))
    half = len(digits) // 2
    second = digits[half::] if len(digits) % 2 == 0 else digits[half + 1::]

    return sum(digits[0:half]) == sum(second)


def number_to_list(n):
    return list(map(int, str(n)))
