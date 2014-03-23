def count_vowels(str):
    vowels = 'aeiouy'
    all_vowels = vowels + vowels.upper()
    return count_letters_in_string(str, all_vowels)


# Solution 1
def count_letters_in_string(string, letters):
    return sum(map(lambda letter: string.count(letter), letters))


# Solution 2
# def count_letters_in_string(string, letters):
#     count = 0
#     for char in string:
#         if char in letters:
#             count += 1

#     return count
