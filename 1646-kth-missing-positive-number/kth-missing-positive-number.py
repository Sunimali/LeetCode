class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # cur_k = 0
        # prev = 0
        # for i, n in enumerate(arr):
        #     dif = n - prev
        #     if dif == 1:
        #         prev = n
        #         continue
        #     dif = dif - 1
        #     temp =  cur_k + dif
        #     if temp < k:
        #         cur_k = temp
        #         prev = n
        #     else:
        #         return prev + (k- cur_k)
        # if cur_k == 0:
        #     return prev + k
        # if cur_k < k:
        #    return prev + (k- cur_k)

        #binary search solution

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right)//2
            missing = arr[mid] - mid - 1
            
            if missing < k: #move to right
                left = mid + 1
            else:
                right = mid - 1
        return k + left
                




           



