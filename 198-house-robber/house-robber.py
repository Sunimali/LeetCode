class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        cache = {}
        return self.rob_rec(cache,nums, size - 1)
    
    def rob_rec(self, cache, nums, i ):

        if i in cache:
            return cache[i]
        if i ==  0:
            cache[i] = nums[i]
            return cache[i] 
        if(i<0):
            return 0
        else:
            skipped = self.rob_rec(cache, nums,i-1)
            robbed = nums[i] + self.rob_rec(cache, nums, i-2)
            cache[i] = (max(skipped, robbed))
            return cache[i]

        
        