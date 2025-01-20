class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        size = len(nums)

        if size == 1:
            return nums[0]
        if size ==0:
            return 0
       
        maj = size//2
        for i in range(size):
            if nums[i] in dic:
                dic[nums[i]] = dic[nums[i]] + 1
                if maj < dic[nums[i]]:
                    return nums[i]
            else:
                dic[nums[i]] = 1
        return 0

        