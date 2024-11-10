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

         #iterative method 

        # h = self.depth(root)
        # answer = []
        # for i in range(1,h+1):
        #     ans = []
        #     self.traversal(root,i, ans)
        #     answer.append(ans)
        # return answer

    #     level = 0
    #     ans = []
    #     self.traverse(root,level,ans)
    #     return ans

    # def traverse(self, root, level, ans):
    #     if root is None:
    #         return
    #     if level == len(ans):
    #         ans.append([])
    #     ans[level].append(root.val)
    #     self.traverse(root.left, level+1, ans)
    #     self.traverse(root.right, level+1,ans) 
            
  

    # def traversal(self, root, level, ans):
    #     if root is None:
    #         return
    #     elif level == 1:
    #         ans.append(root.val)
    #     else:
    #         self.traversal(root.left, level-1, ans)
    #         self.traversal(root.right, level-1, ans)                

    # def depth(self,root):
    #     if root is None:
    #         return 0
    #     else:
    #         return 1+ max(self.depth(root.left), self.depth(root.right))           
