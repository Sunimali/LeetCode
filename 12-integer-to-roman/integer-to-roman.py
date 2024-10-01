class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #dictoinary to map int to roman letters
        roman = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        numbers = (1000,900,500,400,100,90,50,40,10,9,5,4,1) #numbers need to divide iteratively
        str ="" #initial string
        rem = num #remainder
        i = 0
        while rem > 0: #devide until remainder is 0
            key = numbers[i]
            count = rem // key
            rem = rem%key
   
            i = i+1
            if(count == 0): #skip relavant roman charater
                continue
            if(count < 4): #if count>3 go to the substractive form
                str  =  str + count*roman.get(key) #add charaters accroding to the count
 
        return str
        