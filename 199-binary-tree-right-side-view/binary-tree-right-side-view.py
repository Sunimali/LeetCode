# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        q = deque()
        ans = []
        if root:
            q.append(root)
        else:
            return ans
        while len(q) != 0:
            self.traverse(q,ans)
        return ans

    def traverse(self,q,ans):
        size = len(q)
        t = None
        for _ in range(size):
            t = q.popleft()
            if t.left:
                q.append(t.left)
            if t.right:    
                q.append(t.right)
        ans.append(t.val)   
 


        