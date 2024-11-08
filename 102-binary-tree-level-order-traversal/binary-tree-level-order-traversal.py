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
        queue = []
        answer = []

        queue.append(root)
        while queue: #if not empty
            size = len(queue)
            ans = []

            for i in range(size):
                t = queue.pop(0)
                if t is not None:
                    ans.append(t.val)
                    queue.append(t.left)
                    queue.append(t.right)  
            if ans:
                answer.append(ans)
        return answer    
