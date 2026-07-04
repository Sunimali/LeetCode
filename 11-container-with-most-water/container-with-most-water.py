class Solution:
    def maxArea(self, height: List[int]) -> int:
        cur_max = 0
        l = 0
        r = len(height) - 1

        while l < r:
            area = min(height[l], height[r]) *  (r- l)
            cur_max  = max(cur_max, area)

            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        
        return cur_max
        


        