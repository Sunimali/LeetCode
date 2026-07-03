class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cur_max = 0
        f = 0
        s = 0
        cur_k = 0
        prev_s = 0
        count = 0

        if k == 0:
            for num in nums:
                if num == 0:
                    cur_max = max(cur_max, count)
                    count = 0
                else:
                    count+=1
            cur_max = max(cur_max, count)
            return cur_max

        while s < len(nums) and f < len(nums):
            # print(f"cur k{cur_k}")
            while s < len(nums) and cur_k <= k:
                # print(f"s,{s} and f {f} curk {cur_k}")
                if nums[s] == 0:
                    cur_k += 1

                if cur_k == k:
                    prev_s = s - 1

                if cur_k > k:
                    break

                s += 1

            if s < len(nums) and s - prev_s == 1:
                s = prev_s
            else:
                s = s - 1

            size = s - f + 1
            cur_max = max(cur_max, size)
            # print(f"cur_max is, {cur_max} curent k {cur_k}")
            # print(f"s {s}")
            # print(f"f {f}")

            if f < len(nums) and nums[f] == 0:
                nums[f] = 1
                f += 1
            else:
                while f < len(nums) and nums[f] == 1:
                    f += 1
                if f < len(nums):
                    nums[f] = 1
                    f += 1

            cur_k -= 2
            s = s + 1

        return cur_max

  



            

