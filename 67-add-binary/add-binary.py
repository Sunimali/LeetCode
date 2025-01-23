class Solution:
    def addBinary(self, a: str, b: str) -> str:

        size_a = len(a)
        size_b = len(b)
        
        out = ""

        if size_a ==0: #handle empy
            return b
        if size_b == 0:
            return a

        if size_a >= size_b:
            diff = size_a - size_b
            return self.find_answer(a, b, out, diff, size_a)
        else:
            diff = size_b - size_a
            return self.find_answer(b, a, out, diff, size_b)


    def find_answer(self,l,s,out,diff,l_size):
        carry = 0
        while(l_size > 0):
   
            if l_size <= diff :
                ans = int(l[l_size -1]) + carry
            else:
                ans = int(l[l_size - 1])+ int(s[l_size - diff - 1]) + carry

            if ans > 1:
                carry = ans// 2

                out = str(ans%2) + out 
            else:
                out = str(ans) + out
                carry = 0 
            l_size = l_size - 1
        
        if carry != 0:
            out = str(carry) + out  
        return out



        