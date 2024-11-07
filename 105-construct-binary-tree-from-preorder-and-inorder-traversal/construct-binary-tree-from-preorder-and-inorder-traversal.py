# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder:
            return None
        #find the root
        t =  TreeNode(preorder[0]) #get the forst node is pre order list

        index = inorder.index(preorder[0]) #find the root index from preoder

        inorder_left = inorder[:index] #divide and find new inorder and pre over
        inorder_right = inorder[index+1:]

        preorder_left = preorder[1:1+ index]
        preorder_right = preorder[1+ index:]

        #create left subtree
        t.left = self. buildTree(preorder_left,inorder_left)
        t.right = self. buildTree(preorder_right,inorder_right)

        return t






        
            
                 





            

        