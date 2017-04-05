given_mat = [[999, -1, 0, 999],
             [999, 999, 999, -1],
             [999, -1, 999, -1],
             [0, -1, 999, 999]]


def shortest_dis(matrix):
    queue = []
    visited = [[False for i in range(len(matrix))] for j in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                queue.append((i, j))
                visited[i][j] = True
    update(matrix, visited, queue)

    for row in matrix:
        print(row)


def update(mat, visited, queue):
    pairs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while len(queue) > 0:
        topx, topy = queue.pop(0)

        for xx, yy in pairs:
            x = topx + xx
            y = topy + yy
            # print("(", x, y, ")")
            if 0 <= x < len(mat) and 0 <= y < len(mat[0]):
                if visited[x][y] == False and mat[x][y] != 0 and mat[x][y] != -1:
                    visited[x][y] = True
                    if mat[x][y] > mat[topx][topy] + 1:
                        mat[x][y] = mat[topx][topy] + 1
                    queue.append((x, y))

shortest_dis(given_mat)