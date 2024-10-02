class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        size = len(s)
        str = ""
        first = (numRows + (numRows - 1) )-1 #find the start iterator
        second = 0 #find the second iterator

        if size == 1 or numRows ==1: #retrun string
            return s
        
        for i in range(numRows-1,-1,-1): #iterate through rows
            start = numRows - 1 - i #find intial for each row
            shift = 1 #whether need to shift iterater from first to one
            current = start
            while current < size: #iterate for all characters
                str = str + s[current]
                if(second == 0): #if one iterator is zero keep using none zero iterator without shifting
                    current = current + first
                elif(first == 0):
                    current = current + second
                else: #else shift iterator after one turn
                    if(shift):
                        current = current + first #update current position based on selected iterator
                        shift = 0
                    else:
                        current = current + second
                        shift = 1

            first = first - 2 #update the iterator
            second = second + 2        
        return str
               




        