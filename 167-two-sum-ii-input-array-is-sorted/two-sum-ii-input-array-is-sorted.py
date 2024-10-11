class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(numbers)
        f = 0 #pointer for start numbers
        e = size -1 #pointer for end numbers

        while(f!=size):
            temp_sum = numbers[e]+ numbers[f]
            if(temp_sum>target): #if sum is larger than target only move end pointer
                e = e - 1
            elif(temp_sum<target):#if sum is samller than target only move start pointer
                f = f + 1
            else:
                break  
        return [f+1,e+1] #since 1 index array

        

        