# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        ans = self.traverse(root,p,q)
        return ans
        
    def traverse(self,root,p,q):
        if root is None:
            return 
        else:
            if root == p:
                return root
            elif root == q:
                return root   
            else:
                left = self.traverse(root.left,p,q) 
                right = self.traverse(root.right,p,q)

                if right and left:
                    return root
                elif right:
                    return right
                elif left:
                    return left
                else:
                    return None        


