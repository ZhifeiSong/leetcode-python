from typing import List
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        nodeToVisit = deque()
        nodeToVisit.append((0, 0, 1)) #each node is a tuple with (row, column, path_count)
        visited = [[False for _ in range(n)] for _ in range(n)]
        visited[0][0] = True
        while nodeToVisit:
            (r, c, path_count) = nodeToVisit.popleft()
            if r == n-1 and c == n-1: # reach the end node
                return path_count
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if (0<=r+x<n and 0<=c+y<n and grid[r+x][c+y]==0 and visited[r+x][c+y] is False):
                        nodeToVisit.append((r+x, c+y, path_count+1))
                        visited[r+x][c+y] = True
        return -1

solution = Solution()
assert solution.shortestPathBinaryMatrix([[0]]) == 1
assert solution.shortestPathBinaryMatrix([[0,1],[1,0]]) == 2
assert solution.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]) == 4
assert solution.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]) == -1