class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        count = 0
        count = self.rec_climb( cache,n)

        return count
    def rec_climb(self,cache,n):
        if n in cache:
            return cache[n]
        if n == 0:
            return 1
        elif n<0:
            return 0
        else:
            cache[n] = (self.rec_climb(cache, n -1) + self.rec_climb(cache, n - 2))
            return cache[n]

            
            
