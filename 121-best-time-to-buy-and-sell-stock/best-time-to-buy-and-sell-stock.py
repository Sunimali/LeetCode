class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = prices[0]
        max = prices[0]
        profit = 0
        for i in prices:
            if(min > i):
                min = i
                max = i
            if(max < i):
                max = i 
                temp = max - min
                if(temp > profit):
                    profit = temp
        return profit            

        