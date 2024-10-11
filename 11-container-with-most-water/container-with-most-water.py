class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        f = 0
        e = size -1
        area = 0

        while(e!=f):

            min_index = 0
            current_area = 0
            if(height[f] <= height[e]):
                min_index = f
                current_area = height[min_index]* (e - f)
                f = f + 1 #move the minimum hieght
            else:
                min_index = e
                current_area = height[min_index]* (e - f)
                e = e - 1 #move the minimum hieght
            if(current_area> area): #check current area with perius max area value
                area = current_area
        return area               
            

        