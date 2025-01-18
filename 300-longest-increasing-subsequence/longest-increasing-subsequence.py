class Solution(object):

    def binary_search(self, nums, first, last, key):
        mid = (last + first)//2
        if first > last:
            return first
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            return self.binary_search(nums, mid+1, last, key)
        else:
            return self.binary_search(nums, first, mid-1, key)

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub = []
     
        for i in nums:
            if sub:
                if i > sub[len(sub) - 1]:
                    sub.append(i)
                elif i < sub[len(sub) - 1]:
                    lowest = self.binary_search(sub, 0, len(sub)-1, i)
                    sub[lowest] = i
                else:
                    continue
            else:
                sub.append(i)
        return len(sub)

        