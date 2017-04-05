mtr = [[1,0,1],
       [0,1,0],
       [1,0,1]]

def largest_x(matrix, x, y):
    def getDiagonal(x,y,i,j):
        if x >= 0 and y >= 0 and x < len(matrix) and y < len(matrix[0]):
            return 1 + getDiagonal(x+i,y+j,i,j) if matrix[x][y]==1 else 0
        else:
            return 0

    if matrix[x][y] == 1:
        top_left = getDiagonal(x,y,-1,-1)
        top_right = getDiagonal(x,y,-1,1)
        bottom_left = getDiagonal(x,y,1,-1)
        bottom_right = getDiagonal(x,y,1,1)
        return min(top_left, top_right, bottom_left, bottom_right)
    else:
        return 0

ans = -1
for i in range(len(mtr)):
    for j in range(len(mtr[0])):
        ans = max(ans, largest_x(mtr, i, j))
print(ans)
