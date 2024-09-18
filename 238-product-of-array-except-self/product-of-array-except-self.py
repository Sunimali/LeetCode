import copy
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        postNum = [1]* size

        for i in range(size-1,-1,-1):
            if(i==size-1):
                postNum[i] = nums[i]
            else:
                postNum[i] = nums[i]* postNum[i+1]
        preMul = 1
        for i in range(size):
            if(i==size-1):
                nums[i] = preMul
            else:    
                temp =  preMul * nums[i]
                nums[i] = preMul * postNum[i+1]
                preMul = temp

        return nums