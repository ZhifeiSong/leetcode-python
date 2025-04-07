from typing import List
from sortedcontainers import SortedList
from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_map = defaultdict(SortedList)
        def digitSum(num: int) -> int:
            sum = 0
            while num:
                sum += num%10
                num //= 10
            return sum
        for num in nums:
            digit_sum_map[digitSum(num)].add(num)
        max_sum = -1
        for list in digit_sum_map.values():
            if len(list) >= 2:
                max_sum = max(max_sum, list[-1] + list[-2])
        return max_sum

solution = Solution()
print(solution.maximumSum([10,12,19,14]))
