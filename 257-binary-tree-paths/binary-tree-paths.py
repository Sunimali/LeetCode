# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        ans = []
        def preorder(node, st):
            if node is None:
                return ""
            else:
                if node.right is None and node.left is None:
                    st = st + str(node.val)
                    ans.append(st)
                    return st
                else:
                    st = st + str(node.val) + "->"
                    preorder(node.left, st)
                    preorder(node.right, st)
            
        preorder(root, "")
        return ans
        
        