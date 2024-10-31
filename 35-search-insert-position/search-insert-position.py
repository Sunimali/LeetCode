class Solution(object):

    def insert(self,start,end,nums,target):
      
        if(start>=end):
            return end
        mid = (end - start)//2 
        
        if(nums[mid]>target): #need to move left
            end = start+mid
            if(len(nums)==1 or len(nums)==0):
                return start     
            return self.insert(start,start+mid,nums[:mid], target)
        elif (nums[mid]<target): #need to move  right
            start = start+mid+1
            if(len(nums)==1 or len(nums)==0) :
                return end
            return self.insert(start,end,nums[mid+1:], target)
        else:
            return start+mid

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.insert(0,len(nums),nums,target)
           

        