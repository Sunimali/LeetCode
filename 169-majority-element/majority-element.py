class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        count = len(nums)//2 + 1
        print(count)

        for n in nums:
            if n in dic:
                dic[n] =  dic[n] + 1
            else:
                dic[n] = 1
            if dic[n] >= count:
                    return n