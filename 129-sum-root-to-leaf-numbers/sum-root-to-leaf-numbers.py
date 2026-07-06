# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        ans = []
        total = 0
        st = ""
        def preorder(node, st):
            if node is None:
                return ""
            if node.left is None and node.right is None: #leaf node
                st  = st + str(node.val)
                val  = int(st)
                ans.append(val)
                return
            else:
                st = st + str(node.val)
                preorder(node.left, st)
                preorder(node.right, st)
        
        preorder(root, st)

        for s in ans:
            total+= s
        return total

        




        