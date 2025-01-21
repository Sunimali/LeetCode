class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        size = len(nums)
        if size == 1:
            return 0
        if size == 0:
            return
        return self.binary_search(nums, 0, size - 1 )
      

    def binary_search(self, nums, first, last):

        mid = first + (last - first) // 2

        if mid == 0:
            if nums[mid+1] < nums[mid]:
                return mid
            else:
                return self.binary_search(nums,mid+1, last)
        
        if mid == len(nums)-1:
            if nums[mid-1] < nums[mid]:
                return mid
            else:
                return self.binary_search(nums,first, mid)
      
        if nums[mid+1] < nums[mid] and nums[mid-1] < nums[mid]:
            return mid

        else:
            if nums[mid+1] > nums[mid-1]:
                return self.binary_search(nums,mid+1, last)
            else:
                return self.binary_search(nums,first, mid)

        return 
            

        



        




        