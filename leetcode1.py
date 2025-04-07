from collections import deque
from collections import defaultdict
from typing import List
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createTree(inOrderList, nodeIndex):
    if nodeIndex < len(inOrderList):
        if inOrderList[nodeIndex] is None:
            return None
        else:
            leftNode = createTree(inOrderList, nodeIndex * 2 + 1)
            rightNode = createTree(inOrderList, nodeIndex * 2 + 2)
            return TreeNode(inOrderList[nodeIndex], leftNode, rightNode)
    else:
        return None

root1 = createTree([3,9,20,None,None,15,7],0)
root2 = createTree([3,9,8,4,0,1,7],0)
root3 = createTree([3,9,8,4,0,1,7,None,None,None,2,5], 0)
print(root3)

colTable = defaultdict(list)

queue = deque([(root1,0)])
while queue:
    node, col = queue.popleft()
    if node is not None:
        colTable[col].append(node.val)
        queue.append((node.left, col-1))
        queue.append((node.right, col+1))

ret = [colTable[k] for k in sorted(colTable.keys())]
print(ret)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        distanceMatrix = [[-1] * len(matrix[0]) for i in range(len(matrix))]
        longest = 1
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if distanceMatrix[m][n] == -1:
                    distanceMatrix[m][n] = self.exploreMatrix(matrix, distanceMatrix, m, n)
                    longest = max(distanceMatrix[m][n], longest)
        return longest

    def exploreMatrix(self, matrix: List[List[int]], distanceMatrix: List[List[int]], m: int, n: int) -> int:
        leftLen, topLen, rightLen, botLen = 0, 0, 0, 0
        if m > 0 and matrix[m][n] < matrix[m - 1][n]:
            if distanceMatrix[m - 1][n] > 0:
                topLen = 1 + distanceMatrix[m - 1][n]
            else:
                topLen = 1 + self.exploreMatrix(matrix, distanceMatrix, m - 1, n)
        if n > 0 and matrix[m][n] < matrix[m][n - 1]:
            if distanceMatrix[m][n - 1] > 0:
                leftLen = 1 + distanceMatrix[m][n - 1]
            else:
                leftLen = 1 + self.exploreMatrix(matrix, distanceMatrix, m, n - 1)
        if m < len(matrix) - 1 and matrix[m][n] < matrix[m + 1][n]:
            if distanceMatrix[m + 1][n] > 0:
                botLen = 1 + distanceMatrix[m + 1][n]
            else:
                botLen = 1 + self.exploreMatrix(matrix, distanceMatrix, m + 1, n)
        if n < len(matrix[0]) - 1 and matrix[m][n] < matrix[m][n + 1]:
            if distanceMatrix[m][n + 1] > 0:
                rightLen = 1 + distanceMatrix[m][n + 1]
            else:
                rightLen = 1 + self.exploreMatrix(matrix, distanceMatrix, m, n + 1)
        distanceMatrix[m][n] = max(leftLen, topLen, rightLen, botLen, 1)
        return distanceMatrix[m][n]

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        deleted = False
        while i < j:
            if s[i] != s[j]:
                if deleted:
                    return False
                elif s[i + 1] == s[j] and s[i+2] == s[j-1]:
                    i += 1
                    deleted = True
                elif s[i] == s[j - 1] and s[i+1] == s[j-2]:
                    j -= 1
                    deleted = True
                else:
                    return False
            i += 1
            j -= 1
        return True

    def infixToRPN(self, s:str) -> list[str]:
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        rpn = []
        opStack = []
        currNum = []
        for i in range(len(s)):
            if s[i].isnumeric():
                currNum.append(s[i])
            else:
                if currNum:
                    rpn.append(''.join(currNum))
                    currNum = []
                if s[i] in precedence.keys():
                    while opStack and precedence[opStack[-1]] >= precedence[s[i]]:
                        rpn.append(opStack.pop())
                    opStack.append(s[i])
        if currNum:
            rpn.append(''.join(currNum))
        while opStack:
            rpn.append(opStack.pop())
        return rpn

    def evalRPN(self, rpnList:list[str]) -> int:
        #RPN has to be valid
        stack = []
        for s in rpnList:
            if s.isnumeric():
                stack.append(s)
            if s in '+-*/':
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                if s == '+':
                    res = operand1 + operand2
                elif s == '-':
                    res = operand1 - operand2
                elif s == '*':
                    res = operand1 * operand2
                else:
                    res = int(operand1 / operand2)
                stack.append(res)
        return stack.pop()

    def simplifyPath(self, path: str) -> str:
        stack = []
        start, end = 0, 1
        while end < len(path):
            while end < len(path) and path[end] != '/':
                end += 1
            dirName = path[start + 1:end]
            if dirName:
                if dirName == '..':
                    if stack:
                        stack.pop()
                elif dirName != '.':
                    stack.append(dirName)
            start = end
            end += 1
        return '/' + '/'.join(stack)

    def treeDFSInorder(self, root:Optional[TreeNode]) -> None:
        if root:
            self.treeDFSInorder(root.left)
            print(root.val)
            self.treeDFSInorder(root.right)

s=None
if not s:
    print("empty string will be evaluate as false")
solution = Solution()
print(solution.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
assert solution.validPalindrome("cuppucu") == True
assert solution.validPalindrome("abc") == False
assert solution.validPalindrome("aba") == True
stringList = solution.infixToRPN(" 3+5 / 2 ")
print(stringList)
print(solution.evalRPN(stringList))
print(solution.simplifyPath('/.../a/../b/c/../d/./'))

class SparseVector:
    def __init__(self, nums: List[int]):
        self.dict = {}
        for i in range(len(nums)):
            self.dict[i] = nums[i]
    def dotProduct(self, vec:'SparseVector') -> int:
        product = 0
        '''
        if len(self.dict) > len(vec.dict):
            sd, ld = vec.dict, self.dict
        else:
            sd, ld = self.dict, vec.dict
        '''
        sd, ld = (vec.dict, self.dict) if len(self.dict) > len(vec.dict) else (self.dict, vec.dict)
        for k in sd:
            if k in ld:
                product += self.dict[k] * vec.dict[k]
        return product
v1 = SparseVector([1,0,0,2,3])
v2 = SparseVector([0,3,0,4,0])
print(v1.dotProduct(v2))
a = deque()
a.append(2)
a.append(3)
print(a.popleft())

