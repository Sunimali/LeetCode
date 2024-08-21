class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        size = len(nums)
        last = size 
        i = 0
        while(last != i):
            if(nums[i] == val):
                nums[i] = nums[last-1]
                last = last - 1
                if(nums[i] != val):
                    i = i + 1
            else:
                i = i + 1
        del nums[i:size] 
        
                
        