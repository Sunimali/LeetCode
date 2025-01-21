class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        size = len(nums)
        if size ==0:
            return None
        if size == 1:
            return 0
        for i in range(size):
            if i == 0: #first number
                if nums[i] > nums[i+1]:
                    return i
            if i == size - 1: #last number
                if nums[i] > nums[i-1]:
                    return i
            
            if nums[i] > nums[i+1] and nums[i] > nums[i-1]: #middle
                return i

        