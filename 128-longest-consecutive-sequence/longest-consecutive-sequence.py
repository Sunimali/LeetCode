import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        visited = set()
        d = {}
        len_max = 0

        for num in s:
            cur = num
            if cur in visited:
                continue
            else:
                visited.add(cur)

            while cur in s:
                cur += 1
                visited.add(cur)
                if cur in d:
                    d[num] = d[cur]
                    d.pop(cur)
                    break
            if num not in d:       
                d[num] = cur

        for i in d:
            len_max = max(len_max, d[i] - i)
        return len_max


    

        
            

            

            
        