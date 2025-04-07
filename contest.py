from typing import List
class Solution:
    def minimize_max_difference(self, nums:List[int]):
        # Early check: If there are no missing values (-1), return max absolute difference
        if -1 not in nums:
            return max(abs(nums[i] - nums[i + 1]) for i in range(len(nums) - 1))

        def is_feasible(D):
            # Check if there exists a pair (x, y) with max difference <= D
            min_val, max_val = 1, 10 ** 9  # Range for x, y
            for i in range(len(nums)):
                if nums[i] == -1:
                    # For adjacent non-missing values, restrict x, y
                    if i > 0 and nums[i - 1] != -1:
                        min_val = max(min_val, nums[i - 1] - D)
                        max_val = min(max_val, nums[i - 1] + D)
                    if i < len(nums) - 1 and nums[i + 1] != -1:
                        min_val = max(min_val, nums[i + 1] - D)
                        max_val = min(max_val, nums[i + 1] + D)
                else:
                    if i > 0 and nums[i - 1] == -1:
                        min_val = max(min_val, nums[i] - D)
                        max_val = min(max_val, nums[i] + D)
                if i > 0 and nums[i] == -1 and nums[i - 1] == -1:
                    min_val = max(min_val - D, 1)
                    max_val = min(max_val + D, 10 ** 9)
                # If the range collapses, return False
                if min_val > max_val:
                    return False
            # Check if we can find valid x, y
            return True

        # Binary search for the minimum maximum difference
        left, right = 0, 10 ** 9
        while left < right:
            mid = (left + right) // 2
            if is_feasible(mid):
                right = mid  # Try a smaller D
            else:
                left = mid + 1  # Increase D

        return left

solution = Solution()
print(solution.minimize_max_difference([-1, -1, 13, 34]))