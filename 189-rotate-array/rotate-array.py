class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        checked = [False for i in range(size)]
        itr = 0
        temp = nums[0]
        i = 0
        while(i != size):
            next = itr+ k
            if(next > size-1):
                next = next % size 
            if(checked[next]):
                temp = nums[itr+1]
                itr = itr+1
        
            else: 
                temp1 = nums[next]
                nums[next] = temp
            
                checked[next] = True
                temp = temp1
                itr = next 
                i = i + 1 
               
            
        