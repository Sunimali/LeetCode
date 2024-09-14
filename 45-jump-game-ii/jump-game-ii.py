class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        jump = 0
        itr = 0
        size = len(nums)


        while itr < size-1:
            nextMaxItr = itr + nums[itr]

            if nextMaxItr>=size-1:
                jump = jump+1
                return jump
            else:    
                maxjump = nextMaxItr + nums[nextMaxItr]
            
            maxindex = nextMaxItr
            
            for i in range(nextMaxItr, itr ,-1):
                curJump = i + nums[i]
                
                if curJump > maxjump:
                    maxjump = curJump
                    maxindex = i
            jump = jump + 1
            itr  = maxindex
                   
        return jump