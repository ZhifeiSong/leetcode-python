from typing import List
def countSquares(matrix: List[List[int]]) -> int:
    row = len(matrix)
    col = len(matrix[0])
    grid = [[0] * col for _ in range(row)]
    count = 0
    for i in range(row):
        for j in range(col):
            if i == 0 or j == 0:
                grid[i][j] = matrix[i][j]
            else:
                if matrix[i][j] == 1:
                    grid[i][j] = min(grid[i - 1][j], grid[i - 1][j - 1], grid[i][j - 1]) + 1
                else:
                    grid[i][j] = 0
            count += grid[i][j]
    return count

print(countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))