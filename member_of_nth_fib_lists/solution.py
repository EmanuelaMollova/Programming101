def member_of_nth_fib_lists(listA, listB, needle):
    i = 0
    while len(nth_fib_lists(listA, listB, i)) <= len(needle):
        if needle in nth_fib_lists(listA, listB, i):
            return True
        else:
            i += 1

    return False


def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    elif n == 2:
        return listB
    else:
        fib_lists = [listA, listB]

        for i in range(2, n):
            fib_lists.append(fib_lists[i-2] + fib_lists[i-1])

        return fib_lists[n - 1]
