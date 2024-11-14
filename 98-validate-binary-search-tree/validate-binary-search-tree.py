# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.traverse(root,float('-inf'),float('inf'))
    def traverse(self,root,minv,maxv):
        if root is None:
            return True
        else:
            if root.val > minv and root.val < maxv:
                return self.traverse(root.left,minv,root.val) and self.traverse(root.right,root.val,maxv)
            else:
                return False     


        