def magic_square(matrix):
    sums = [
        sum_of_forward_main_diagonal(matrix),
        sum_of_backward_main_diagonal(matrix)
    ] + sum_of_rows(matrix) + sum_of_columns(matrix)

    return len(set(sums)) == 1


def sum_of_forward_main_diagonal(matrix):
    return sum(matrix[i][i] for i in range(len(matrix[0])))


def sum_of_backward_main_diagonal(matrix):
    size = len(matrix[0])
    return sum(matrix[size-i-1][i] for i in range(len(matrix[0])))


def sum_of_rows(matrix):
    return list(map(lambda row: sum(row), matrix))


def sum_of_columns(matrix):
    return sum_of_rows(list(zip(*matrix)))
