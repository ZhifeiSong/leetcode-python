'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
Example 1:

  1 2 3
  4 5 6
  7 8 9
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
'''
from typing import List
from collections import defaultdict
class Solution:
    def findDiagonalOrder1(self, mat: List[List[int]]) -> List[int]:
    # key observation matrix indices on diagonal line have equal sums, i.e. in example 1, the indices of 2 and 4 both have sum 2.
        diagonals = defaultdict(list)
        diagonal_traverse = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonals[i+j].append(mat[i][j])
        for i in range(len(mat) + len(mat[0]) -1):
            if i%2 == 0:
                diagonals[i].reverse()
            diagonal_traverse.extend(diagonals[i])
        return diagonal_traverse

solution = Solution()
assert solution.findDiagonalOrder1([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,4,7,5,3,6,8,9]
assert solution.findDiagonalOrder1([[1,2],[3,4]]) == [1,2,3,4]