'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.


Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.

'''
from typing import List
class Solution:
    def neighbors(self, row: int, column: int, n:int) -> list:
        for nr, nc in [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]:
            if 0 <= nr < n and 0 <= nc < n:
                yield (nr, nc)

    def dfs(self, r: int, c: int, index: int, grid: List[List[int]]) -> int:
        area = 1
        grid[r][c] = index
        for (nr, nc) in self.neighbors(r, c, len(grid)):
            if grid[nr][nc] == 1:
                area += self.dfs(nr, nc, index, grid)
        return area

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def neighbors(row: int, column: int) -> list:
            for nr, nc in [(row-1, column), (row+1, column), (row, column-1), (row, column+1)]:
                if 0<=nr<n and 0<=nc<n:
                    yield (nr, nc)

        def dfs(r:int, c:int, index:int) -> int:
            area = 1
            grid[r][c] = index
            for (nr, nc) in neighbors(r,c):
                if grid[nr][nc] == 1:
                    area += dfs(nr, nc, index)
            return area

        index = 2
        group_size = {}
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    group_size[index] = dfs(r, c, index)
                    index += 1

        answer = max(group_size.values() or 0)
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for (nr, nc) in neighbors(r,c) if grid[nr][nc] > 1}
                    answer = max(answer, sum(group_size[i] for i in seen))
        return answer

solution = Solution()
assert set(solution.neighbors(0, 1, 3)) == {(1, 1), (0, 0), (0, 2)}
assert solution.dfs(0, 0, 2, [[1,0],[0,1]]) == 1
assert solution.dfs(2, 2, 2, [[0,0,1,0,1],[0,1,1,0,0],[0,1,1,0,0],[1,1,1,1,0],[0,0,1,0,0]]) == 10

group_size = {}
a = max(group_size.values() or [0])
print(a)