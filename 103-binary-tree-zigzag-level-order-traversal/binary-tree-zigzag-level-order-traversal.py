# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        q = deque()
        answer = []
        if root: #tree is empty
            q.append(root)
        else:
            return answer
        left = 0
        
        while len(q) != 0: #until q is empty
            size = len(q)
            ans = []

            if left == 1: #change the order left or right
                left = 0
            else:
                left = 1  
            ans = [] 
            for _ in range(size):
                t = None
                t = q.popleft()
                
                ans.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            if left:
                answer.append(ans)
            else:
                ans.reverse()
                answer.append(ans)

        return answer       



        