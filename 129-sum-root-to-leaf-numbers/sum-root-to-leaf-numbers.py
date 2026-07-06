# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        # ans = []
        # total = 0
        # st = ""
        # def preorder(node, st):
        #     if node is None:
        #         return ""
        #     if node.left is None and node.right is None: #leaf node
        #         st  = st + str(node.val)
        #         val  = int(st)
        #         ans.append(val)
        #         return
        #     else:
        #         st = st + str(node.val)
        #         preorder(node.left, st)
        #         preorder(node.right, st)
        
        # preorder(root, st)

        # for s in ans:
        #     total+= s
        # return total

        ans = []
        total = 0

        def preorder(node, val):
            if node is None:
                return ""
            if node.left is None and node.right is None:
                val = val*10 + node.val
                ans.append(val)
            else:
                val = val*10 + node.val
                preorder(node.left, val)
                preorder(node.right, val)
        
        preorder(root, 0)

        for s in ans:
            total += s
        return total


        




        