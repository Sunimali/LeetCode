class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dic = {}
        ans = []

        for item in nums:
            if item in dic:
                dic[item] = dic[item] + 1
            else:
                dic[item] = 1
            
        sorted_dic = sorted(dic.items(), key = lambda item: item[1])
        sorted_dic = sorted_dic[-k:]
        
        
        for i in range(k):
            key,_ = sorted_dic[i]
            ans.append(key)
        
        return ans



        