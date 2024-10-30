# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        ans = [] #initial answer for means root level has mean as root value
        queue = [root] #maintain a queue to store level nodes
        level = 0
        while len(queue) != 0 : #go through evel level
            size = len(queue)
            level_sum = 0
        
            for i in range(size): #consider for one level
                current = queue.pop(0)
                level_sum = current.val + level_sum #get the sum of the level
                if(current.left is not None):
                    queue.append(current.left)
                if(current.right is not None):
                    queue.append(current.right)         
            ans.append(level_sum / float(size)) #append mean in a level to resuls array
        return ans             
                   





        