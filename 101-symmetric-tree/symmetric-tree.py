# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.mirror(root.left, root.right)  

    def mirror(self,l,r):
        if r is None and l is None:
            return True
        elif r is None or l is None:
            return False
        else:
            if r.val == l.val:
                x =self.mirror(r.left,l.right)
                y = self.mirror(r.right,l.left)
                return x and y
            else:
                return False     

                


                
        