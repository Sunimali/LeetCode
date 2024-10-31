# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]

        """     
        if(len(nums) is 0 ): #if left for right subtree is empty
            return None
        else: #create substree
            root = TreeNode() #create root node
            root.val = nums[len(nums)//2] 
        
            root.left =  self.sortedArrayToBST(nums[0:len(nums)//2]) # add left subtree
            root.right = self.sortedArrayToBST(nums[len(nums)//2+1: len(nums)]) #add right
            return root #return subtree
        