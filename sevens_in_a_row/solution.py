def sevens_in_a_row(arr, n):
    i = 0
    while i < len(arr):
        if arr[i] == 7:
            j = i
            count = 0
            while j < len(arr) and arr[j] == 7:
                count += 1
                j += 1
            if count == n:
                return True
            else:
                i = j
        else:
            i += 1

    return False
