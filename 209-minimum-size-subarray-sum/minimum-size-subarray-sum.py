class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        first = 0
        last  = 0
        current_sum = nums[0]
        size = len(nums)

        curr_max = size + 1

        while(last <= size-1):
            if(current_sum >= target):

                inter = last - first + 1
                if(inter< curr_max):
                    curr_max = inter

                    #remove elements from front
                while(current_sum >=target):
                    
                    inter = last - first + 1
                    if(inter < curr_max):
                        curr_max = inter
                    current_sum = current_sum - nums[first]
                    first = first + 1

            else:
                if(last == size - 1):
                    if curr_max>size:
                        return 0
                    return curr_max
                last = last + 1
                current_sum = current_sum + nums[last]
        


