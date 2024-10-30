# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.ordered = []  # Track the previous node's value during traversal
        self.itr =0
        self.min_diff = float('inf')  # Initialize min_diff to a large number
    
   
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
       
        if root is None:
            return self.min_diff #return current min diff
        else:
            #in order traversal
            self.getMinimumDifference(root.left) 
            if(self.itr !=0): #skip updating in first element
                if(self.min_diff>abs(root.val - self.ordered[self.itr-1])):
                    self.min_diff = abs(root.val - self.ordered[self.itr-1] )#update diff

            self.ordered.append(root.val)
            self.itr = self.itr+ 1
            self.getMinimumDifference(root.right)
            return self.min_diff
          
    

        