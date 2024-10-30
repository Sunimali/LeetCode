# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is not None:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return 1 + max(left,right) 
        else:
            return 0     
    
        
        