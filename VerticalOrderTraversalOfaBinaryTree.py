'''
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.
'''

from typing import List, Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # Dictionary to store nodes by their column and row
        # Format: {col: {row: [node_values]}}
        nodes = defaultdict(lambda: defaultdict(list))
        
        def dfs(node: TreeNode, row: int, col: int):
            if not node:
                return
            
            # Store node value with its position
            nodes[col][row].append(node.val)
            
            # Recursively process left and right children
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        # Start DFS from root
        dfs(root, 0, 0)
        
        # Process the results
        result = []
        # Sort columns from left to right
        for col in sorted(nodes.keys()):
            column = []
            # For each column, process rows from top to bottom
            for row in sorted(nodes[col].keys()):
                # Sort nodes in the same position by value
                column.extend(sorted(nodes[col][row]))
            result.append(column)
        
        return result

# Test cases
def test_vertical_traversal():
    solution = Solution()
    
    # Test case 1: Simple tree
    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    expected1 = [[9], [3, 15], [20], [7]]
    assert solution.verticalTraversal(root1) == expected1, "Test case 1 failed"
    
    # Test case 2: Complex tree with multiple nodes in same position
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(7)
    
    expected2 = [[4], [2], [1, 5, 6], [3], [7]]
    assert solution.verticalTraversal(root2) == expected2, "Test case 2 failed"
    
    # Test case 3: Empty tree
    assert solution.verticalTraversal(None) == [], "Test case 3 failed"
    
    # Test case 4: Single node
    root4 = TreeNode(1)
    assert solution.verticalTraversal(root4) == [[1]], "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_vertical_traversal()
