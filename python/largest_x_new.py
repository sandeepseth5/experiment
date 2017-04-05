
def traverse_from_top_left(matrix, aux_matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 or j == 0:
                aux_matrix[i][j] = matrix[i][j]
            elif matrix[i][j] == 1 and aux_matrix[i-1][j-1] > 0:
                aux_matrix[i][j] = aux_matrix[i-1][j-1] + 1
            else:
                aux_matrix[i][j] = matrix[i][j]
    return aux_matrix


def traverse_from_top_right(matrix, aux_matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])-1, -1, -1):
            if i == 0 or j == len(matrix[0])-1:
                aux_matrix[i][j] = matrix[i][j]
            elif matrix[i][j] == 1 and aux_matrix[i-1][j+1] > 0:
                aux_matrix[i][j] = aux_matrix[i-1][j+1] + 1
            else:
                aux_matrix[i][j] = matrix[i][j]
    return aux_matrix


def traverse_from_bottom_left(matrix, bottom_left):
    for i in range(len(matrix)-1, -1, -1):
        for j in range(len(matrix[0])):
            if i == len(matrix)-1 or j == 0:
                bottom_left[i][j] = matrix[i][j]
            elif matrix[i][j] == 1 and bottom_left[i+1][j-1] > 0:
                bottom_left[i][j] = bottom_left[i+1][j-1] + 1
            else:
                bottom_left[i][j] = matrix[i][j]
    return bottom_left


def traverse_from_bottom_right(matrix, bottom_right):
    for i in range(len(matrix)-1, -1, -1):
        for j in range(len(matrix[0])-1, -1, -1):
            if i == len(matrix) - 1 or j == len(matrix[0]) - 1:
                bottom_right[i][j] = matrix[i][j]
            elif matrix[i][j] == 1 and bottom_right[i + 1][j + 1] > 0:
                bottom_right[i][j] = bottom_right[i + 1][j + 1] + 1
            else:
                bottom_right[i][j] = matrix[i][j]
    return bottom_right


def largest_x(matrix):
    top_left = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    top_right = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    bottom_left = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    bottom_right = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]

    top_left = traverse_from_top_left(matrix, top_left)
    top_right = traverse_from_top_right(matrix, top_right)
    bottom_left = traverse_from_bottom_left(matrix, bottom_left)
    bottom_right = traverse_from_bottom_left(matrix, bottom_right)

    ans = -1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            ans = max(min(top_left[i][j], top_right[i][j], bottom_left[i][j], bottom_right[i][j]), ans)

    return 2 * ans - 1

mtr1 = [[1, 0, 1, 0, 1],
       [0, 1, 0, 1, 0],
       [1, 0, 1, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 1, 0, 1]]

mtr2 = [[1, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
        ]

print(largest_x(mtr2))
