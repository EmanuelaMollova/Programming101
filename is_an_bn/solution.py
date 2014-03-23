def is_an_bn(word):
    if not word:
        return True
    elif list(filter(lambda x: x != 'a' or x != 'b', word)):
        return False
    else:
        count_a = len(list(filter(lambda x: x == 'a', word)))
        count_b = len(list(filter(lambda x: x == 'b', word)))
        return count_a == count_b
