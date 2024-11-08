# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        h = self.depth(root)
        answer = []
        for i in range(1,h+1):
            ans = []
            self.traversal(root,i, ans)
            answer.append(ans)
        return answer    

    def traversal(self, root, level, ans):
        if root is None:
            return
        elif level == 1:
            ans.append(root.val)
        else:
            self.traversal(root.left, level-1, ans)
            self.traversal(root.right, level-1, ans)                

    def depth(self,root):
        if root is None:
            return 0
        else:
            return 1+ max(self.depth(root.left), self.depth(root.right))       