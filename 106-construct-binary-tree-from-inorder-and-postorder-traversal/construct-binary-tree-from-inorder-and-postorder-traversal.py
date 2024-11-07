# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not postorder:
            return
        root_val = postorder[-1]#get last element
        index = inorder.index(root_val)#find index in postorder

        inorder_left = inorder[:index]
        inorder_right = inorder[index+1:]

        postorder_left = postorder[0: index]
        postorder_right = postorder[index: -1]

        
        t = TreeNode(root_val)
        t.left = self.buildTree(inorder_left, postorder_left)
        t.right = self.buildTree(inorder_right, postorder_right)

        return t

        

        