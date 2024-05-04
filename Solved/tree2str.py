# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treefunc(root):
        if not root:
            return
        
        result = str(root.val)

        if root.left or root.right:
            result += "(" + treefunc(root.left) + ")"
        
        if root.right:
            result += "(" + treefunc(root.right) + ")"
            
        return result
            
root1 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
output1 = treefunc(root1)
print(output1)  # Output: "1(2(4))(3)"