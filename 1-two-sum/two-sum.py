class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        remain = {}
        size = len(nums)

        for i in range(size):
            
            if nums[i] in remain:
                return [remain[nums[i]], i]
            
            remain[target - nums[i]] = i
        return []

            