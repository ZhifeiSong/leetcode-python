from typing import List
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        dp = [[-1 for _ in range(len(target))] for _ in range(len(words[0]))]
        self.numWays_recur(words, target, 0, 0, dp)
        return dp[0][0]%(10**9+7)

    def numWays_recur(self, words: List[str], target:str, wordsIndex: int, targetIndex: int, dp: List[List[int]]) -> int:
        if targetIndex == len(target):
            return 1
        if wordsIndex == len(words[0]) or len(words[0]) - wordsIndex < len(target) - targetIndex:
            return 0
        if dp[wordsIndex][targetIndex] > -1:
            return dp[wordsIndex][targetIndex]
        count = 0
        for word in words:
            if target[targetIndex] == word[wordsIndex]:
                count += 1
        if count > 0:
            count = count * self.numWays_recur(words, target, wordsIndex+1, targetIndex+1, dp)
        dp[wordsIndex][targetIndex] = count + self.numWays_recur(words, target, wordsIndex+1, targetIndex, dp)
        return dp[wordsIndex][targetIndex]

solution = Solution()
print(solution.numWays(["acca","bbbb","caca"],"aba"))
print(solution.numWays(["abba","baab"], "bab"))