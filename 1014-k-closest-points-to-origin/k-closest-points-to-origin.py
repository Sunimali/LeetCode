class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        dic = {}
        ans = []

        for index, item in enumerate(points):
            z = item[0]*item[0] + item[1]*item[1]
            dic[index] = z

        sorted_dic = sorted(dic.items(), key = lambda item:item[1]) 

        print(sorted_dic)

        sorted_dic = sorted_dic[:k]

        print(sorted_dic)

        for i in range(k):
            key, _ = sorted_dic[i]
            ans.append(points[key])
        return ans

        