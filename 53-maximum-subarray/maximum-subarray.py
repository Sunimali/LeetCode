class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max = nums[0]
        current_max = nums[0]

        for i in range(1, len(nums)):
            item = nums[i]
            current_max = max(current_max + item, item)
            global_max = max(current_max, global_max)
        return global_max
        