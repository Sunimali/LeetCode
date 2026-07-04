class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        bday = 0
        sday = 1
        prof = 0

        if len(prices) < 2:
            return 0
        while sday < len(prices): 
            if prices[bday] > prices[sday]: #no profit
                bday = sday
                sday += 1
            else:
                cur_prof = prices[sday] - prices[bday]
                prof = max(cur_prof, prof)
                sday += 1

        return prof
            
        