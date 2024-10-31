class Solution(object):

    def insert(self,start,end,nums,target):
        print(start)
        print(end)
        if(start>=end):
            return end
        

        mid = (end - start)//2 
        
        print(mid)
        print(nums)
        # if(start>end):
        #     return end - 1

        # print(nums[mid])
        # print(target)

      

        if(nums[mid]>target): #need to move left
            print("left")
            # print(nums[:mid])
            
            end = start+mid
            # if(start>end):
            #     return end
            # else: 
            if(len(nums)==1 or len(nums)==0):
                return start     
            return self.insert(start,start+mid,nums[:mid], target)
        elif (nums[mid]<target): #need to move  right
            print("right")
            start = start+mid+1
            if(len(nums)==1 or len(nums)==0) :
                return end
            # if(start>end):
            #     return end
            return self.insert(start,end,nums[mid+1:], target)
        else:
            return start+mid

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.insert(0,len(nums),nums,target)
           

        