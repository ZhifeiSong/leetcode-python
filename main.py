from typing import List
from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        row = len(grid)
        col = len(grid[0])
        min_cost = [[row * col + 1] * col for _ in range(row)]
        min_cost[0][0] = 0
        queue = deque()
        queue.append((0,0))
        while queue:
            x, y = queue.popleft()
            for i in range(len(direction)):
                dx, dy = direction[i][0], direction[i][1]
                nx, ny = x+dx, y+dy
                if 0 <= nx < row and 0 <= ny < col:
                    move_cost = 0 if grid[x][y] == i+1 else 1
                    if min_cost[nx][ny] > min_cost[x][y] + move_cost:
                        min_cost[nx][ny] = min_cost[x][y] + move_cost
                        if nx == row -1 and ny == col-1:
                            return min_cost[nx][ny]
                        if move_cost == 1:
                            queue.append((nx, ny))
                        else:
                            queue.appendleft((nx, ny))
        return min_cost[row-1][col-1]

solution = Solution()
solution.minCost([[1,1,3],[3,2,2],[1,1,4]])