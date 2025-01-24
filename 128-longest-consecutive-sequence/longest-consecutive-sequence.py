class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dic = {}  # Dictionary to store the next consecutive element
        size = len(nums)

     
        for i in range(size):
            if nums[i] not in dic:
                pre = nums[i] - 1
                post =  nums[i] + 1

                if pre in dic:
                    dic[pre] = nums[i]
                if post in dic:
                    dic[nums[i]] = post
    
                else:
                    dic[nums[i]] = None #no consecutive 
        result = 0


        # for num in dic.keys():
        #     # Only process the start of a sequence
        #     if num - 1 not in dic:
        #         temp = 0
        #         current = num
        #         # Follow the "next" pointers to count the sequence length
        #         while current is not None:
        #             temp += 1
        #             current = dic[current]

        #         # Update the maximum sequence length
        #         result = max(result, temp)

        for key in dic.keys():
            # Skip this key if it's not a beginining #this is the key point in alogrithem
           
            if key - 1 in dic:
                continue

            temp = 0
            current = key

            # Traverse the sequence starting from `key`
            while current in dic:
                temp += 1
                current =  dic[current]

            if temp > result:
                result = temp

        return result


            

                    
            