
class Solution:
    def romanToInt(self, s: str) -> int:
        main_dic = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D":500,"M":1000}
        sp_dic = {"IV":4, "IX": 9, "XL":40, "XC":90,"CD":400, "CM":900}
        sp_fdic = {"I","X","C"}

        ans = 0
        i = 0

        while i < len(s):
            print(ans)
            if s[i] in sp_fdic:
                next_i = i + 1
                if  next_i < len(s):
                    sp = s[i] + s[next_i]
                    if sp in sp_dic:
                        ans += sp_dic[sp]
                        i +=2
                        continue
            ans+= main_dic[s[i]]
            i+=1
        
        return ans
            
                    
                
                    




        