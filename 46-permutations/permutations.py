import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        count = 0

        results = self.rec_permute(nums, [],  results )
        return results
        

    def rec_permute(self, nums, current,results ):
        if len(current) == len(nums):

            results.append(current[:])
            
            return results
       
        for item in nums:
            if item in current:
                continue
            else:
                current.append(item)
                self.rec_permute(nums, current,results )
                current.pop()
                 
        return results
           

        
        


        