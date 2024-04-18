# You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.
# Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
# As a reminder, any shorter prefix of a string is lexicographically smaller.
# For example, "ab" is lexicographically smaller than "aba".
# A leaf of a node is a node that has no children.

# Example 1:
# Input: root = [0,1,2,3,4,3,4]
# Output: "dba"

# Example 2:
# Input: root = [25,1,3,1,3,0,2]
# Output: "adz"

# Example 3:
# Input: root = [2,2,1,null,1,0,null,0]
# Output: "abc"

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        


#test cases
root = [0,1,2,3,4,3,4]
print(Solution.smallestFromLeaf(root))
root = [25,1,3,1,3,0,2]
print(Solution.smallestFromLeaf(root))
root = [2,2,1,null,1,0,null,0]
print(Solution.smallestFromLeaf(root))
        