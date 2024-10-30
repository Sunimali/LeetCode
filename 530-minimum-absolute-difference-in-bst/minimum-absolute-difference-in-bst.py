# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.prev = None #pervius node value
        self.min_diff = float('inf')  # Initialize min_diff to a large number
    
   
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
       
        if root is None:
            return self.min_diff #return current min diff
       
        #in order traversal
        self.getMinimumDifference(root.left) 
        if(self.prev is not None): #skip first one since nothing to compare
            if( self.min_diff> root.val - self.prev): #check diff with current
                self.min_diff =  root.val - self.prev
        self.prev = root.val #set the revius value        
        self.getMinimumDifference(root.right)
        return self.min_diff
          
    

        