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

        if not preorder or not inorder:
            return None

        # The first element in preorder is the root node
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find the index of the root in inorder to split left and right subtrees
        root_index_in_inorder = inorder.index(root_val)

        # Elements to the left in inorder are the left subtree
        # Elements to the right in inorder are the right subtree
        left_inorder = inorder[:root_index_in_inorder]
        right_inorder = inorder[root_index_in_inorder + 1:]

        # Use the length of left_inorder to find the corresponding elements in preorder
        left_preorder = preorder[1:1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]

        # Recursively build left and right subtrees
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
            
                 





            

        