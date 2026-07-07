class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cur_k = 0
        prev = 0
        for i, n in enumerate(arr):
            # print(cur_k)
            dif = n - prev
            if dif == 1:
                prev = n
                continue
            dif = dif - 1
            temp =  cur_k + dif
            print(f"n {n}")
            print(f"prev {prev}")
            print(f"dif{dif}")
            print(f"cur {cur_k}") 
            print(f"temp {temp}") 
            if temp < k:
                print("case1\n")

                cur_k = temp
                prev = n
            else:
                print("case2")
                return prev + (k- cur_k)
        if cur_k == 0:
            return prev + k
        if cur_k < k:
           return prev + (k- cur_k)
           



