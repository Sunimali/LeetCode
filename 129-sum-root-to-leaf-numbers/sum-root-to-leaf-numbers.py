# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        current_sum = 0
        num = ""
        current_sum = self.sumrec(root,current_sum,num)
        return current_sum

        
    def sumrec(self,root,current_sum,num):
        if root is None:
            return 0
        elif root.left is None and root.right is None:#leaf node
            num = num + str(root.val)
            current_sum = current_sum + atoi(num)
            return current_sum
        else:
            num = num + str(root.val)
            return self.sumrec(root.left,current_sum,num) + self.sumrec(root.right,current_sum,num)



        