class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = prices[0]
        max = prices[0]
        size = len(prices)
        profit = 0
        tp = 0
        i = 0

        while(i!= size):
    
            if(min > prices[i]):    
                min = prices[i]
                max = prices[i]
                tp = 0 
            elif(prices[i] < max and tp > 0): 
                min = prices[i]
                max = prices[i] 
                tp = 0              
            elif(max < prices[i]):
                max = prices[i]
                temp = max - min
                if(tp < temp):
                    profit = profit - tp
                    tp = temp
                profit = tp + profit
            i = i + 1  
        return profit

        