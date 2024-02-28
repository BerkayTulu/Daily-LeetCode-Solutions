# Given the root of a binary tree, return the leftmost value in the last row of the tree.
# Example 1:
# Input: root = [2,1,3]
# Output: 1

# Example 2:
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7

# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        q = deque([root])
        ans = 0
        while q:
            ans = q[0].val
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans

    
# Input: root = [1,2,3,4,5]
# Output: 4

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()
bottom_left_value = solution.findBottomLeftValue(root)
print(bottom_left_value) # 3

# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)

solution = Solution()
bottom_left_value = solution.findBottomLeftValue(root)

print(bottom_left_value) # 7
