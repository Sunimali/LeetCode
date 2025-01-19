class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        ans = []

        for item in strs:

            item_sort = "".join(sorted(item))

            if item_sort in dic:
                dic[item_sort].append(item)
            else:
                dic[item_sort] = [item]
        for key in dic.keys():
            ans.append(dic[key])

        return ans
            
