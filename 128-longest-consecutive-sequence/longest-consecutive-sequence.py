class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # if not nums:
        #     return 0

        # # Dictionary to store the next number in the sequence
        # num_dict = {}

        # # Add unique numbers and initialize their "next" values
        # for num in nums:
        #     if num not in num_dict:
        #         # Initially, no next number is assigned
        #         num_dict[num] = None
        #         # Update links for consecutive numbers
        #         if num - 1 in num_dict:
        #             num_dict[num - 1] = num
        #         if num + 1 in num_dict:
        #             num_dict[num] = num + 1

        # # Now, find the longest consecutive sequence
        # result = 0

        # for num in num_dict.keys():
        #     # Only process the start of a sequence
        #     if num - 1 not in num_dict:
        #         temp = 0
        #         current = num
        #         # Follow the "next" pointers to count the sequence length
        #         while current is not None:
        #             temp += 1
        #             current = num_dict[current]

        #         # Update the maximum sequence length
        #         result = max(result, temp)

        # return result
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


        for num in dic.keys():
            # Only process the start of a sequence
            if num - 1 not in dic:
                temp = 0
                current = num
                # Follow the "next" pointers to count the sequence length
                while current is not None:
                    temp += 1
                    current = dic[current]

                # Update the maximum sequence length
                result = max(result, temp)

        # for key in dic.keys():
        #     # Skip this key if it's already processed
        #     if dic[key] is None:
        #         continue

        #     temp = 0
        #     current = key

        #     # Traverse the sequence starting from `key`
        #     while current in dic:
        #         temp += 1
        #         next_element = dic[current]
        #         dic[current] = None  # Mark as visited
        #         if next_element is None:
        #             break
        #         current = next_element

        #     if temp > result:
        #         result = temp

        return result


            

                    
            