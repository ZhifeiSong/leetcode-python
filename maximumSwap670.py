'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.



Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.


Constraints:

0 <= num <= 108
'''
import math
class Solution:
    def maximumSwap(self, num: int) -> int:
        digitList = list(str(num))
        for i in range(len(digitList)):
            currDigit = digitList[i]
            maxDigit = '0'
            maxDigitIndex = i
            for j in range(len(digitList)-1, i, -1):
                if digitList[j] > maxDigit:
                    maxDigitIndex = j
                    maxDigit = digitList[j]
            if maxDigit > currDigit:
                digitList[maxDigitIndex] = currDigit
                digitList[i] = maxDigit
                break
        return int("".join(digitList))

solution = Solution()
assert solution.maximumSwap(2736) == 7236
assert solution.maximumSwap(9973) == 9973
assert solution.maximumSwap(0) == 0
assert solution.maximumSwap(1234567) == 7234561
assert solution.maximumSwap(1111111) == 1111111
assert solution.maximumSwap(100) == 100
assert solution.maximumSwap(102) == 201
assert solution.maximumSwap(1993) == 9913
