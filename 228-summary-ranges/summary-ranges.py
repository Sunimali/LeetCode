class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        intl_len = 0 #initial start intervel length
        if(len(nums)==0):
            return ans
        start = nums[0] #initial start point
       
        for i in nums: #iterte through list
            if(start+intl_len == i): #check already in interval
                intl_len = intl_len + 1
            else: #else reset the interval
                if(intl_len==1): #only one value
                    interval = str(start)
                    ans.append(interval)
                else: #there is a range
                    interval = str(start)+"->"+str(start+intl_len-1)
                    ans.append(interval)
                intl_len = 1
                start = i
        #add the final interval        
        if(intl_len==1): #only one value
                    interval = str(start)
                    ans.append(interval)
        else: #there is a range
            interval = str(start)+"->"+str(start+intl_len-1)
            ans.append(interval)  
        return ans        

            
        
            
            



        