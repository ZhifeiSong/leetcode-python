from typing import List
import heapq


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        min_group = 0
        intervals.sort(key=lambda x: x[0])
        min_heap = []
        for interval in intervals:
            while min_heap and interval[0] > min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval[1])
            min_group = max(min_group, len(min_heap))
        return min_group

    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        def is_subsequence(source, pattern) -> bool:
            curr_index = 0
            for c in source:
                if curr_index < len(pattern) and c == pattern[curr_index]:
                    curr_index += 1
            return curr_index == len(pattern)

        ans = 0
        new_source = list(source)
        for idx in targetIndices:
            new_source[idx] == ''
            if is_subsequence(''.join(new_source), pattern):
                ans += 1
        return ans

solution = Solution()
assert solution.minGroups([[441459,446342],[801308,840640],[871890,963447],[228525,336985],[807945,946787],
                          [479815,507766],[693292,944029],[751962,821744]]) == 4
assert solution.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]) == 3
assert solution.minGroups([[1,3],[5,6],[8,10],[11,13]]) == 1

solution.maxRemovals("abbaa", "aba", [0,1,2])