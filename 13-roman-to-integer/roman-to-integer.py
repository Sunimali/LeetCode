class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #dictionary with numeric value
        roman = {
            "I": 1,
            "IV":4,
            "V": 5,
            "IX":9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC":90,
            "C": 100,
            "CD":400,
            "D": 500,
            "CM":900,
            "M":1000
        }

        size = len(s)
        ans = 0
        i = size -1
        while i >= 0:
            if i == 0: # handle strings have odd characters count
                ans = ans + roman.get(s[0])
                i = i - 1
            else:    #get two by two from end of string
                first = s[i-1]
                sec = s[i]
       
                temp = roman.get(first+sec) # check whether it is XV,IV.. 
                if temp is None: # when it is a singal case add only sec
                    ans = ans + roman.get(sec)
                    i = i - 1
                else:
                    ans = ans + temp #get two values together
                    i = i - 2   
        return ans    