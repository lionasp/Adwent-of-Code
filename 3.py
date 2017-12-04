def calculate_sum(cds, array):
    return sum([array[cds[0]][cds[1] + 1],
                array[cds[0] - 1][cds[1] + 1],
                array[cds[0] - 1][cds[1]],
                array[cds[0] - 1][cds[1] - 1],
                array[cds[0]][cds[1] - 1],
                array[cds[0] + 1][cds[1] - 1],
                array[cds[0] + 1][cds[1]],
                array[cds[0] + 1][cds[1] + 1],
                ])


def fill_square(cds, size, array):
    # to top
    for i in range(size):
        array[cds[0] - i][cds[1]] = calculate_sum((cds[0] - i, cds[1]), array)
    # to left
    for i in range(1, size + 1):
        array[cds[0] - size + 1][cds[1] - i] = calculate_sum((cds[0] - size + 1, cds[1] - i), array)
    # to bottom
    for i in range(1, size + 2):
        array[cds[0] - size + i][cds[1] - size] = calculate_sum((cds[0] - size + i, cds[1] - size), array)
    # to right
    for i in range(1, size + 1):
        array[cds[0] + 1][cds[1] - size + i] = calculate_sum((cds[0] + 1, cds[1] - size + i), array)


n = 12
c = (n // 2) - 1
array = [[0] * n for i in range(n)]
array[c][c] = 1
array[c][c + 1] = 1
array[c - 1][c + 1] = 2
array[c - 1][c] = 4
array[c - 1][c - 1] = 5
array[c][c - 1] = 10
array[c + 1][c - 1] = 11
array[c + 1][c] = 23
array[c + 1][c + 1] = 25

fill_square((c + 1, c + 2), 4, array)
fill_square((c + 2, c + 3), 6, array)
fill_square((c + 3, c + 4), 8, array)

for i in range(n):
    print(array[i])
