def count_words(arr):
    result = dict(zip(arr, [0] * len(arr)))

    for word in arr:
        result[word] += 1

    return result
