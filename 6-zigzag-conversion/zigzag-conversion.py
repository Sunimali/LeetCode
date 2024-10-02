class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        size = len(s)
        str = ""
        first = (numRows + (numRows - 1) )-1
        second = 0

        if size == 1 or numRows ==1:
            return s
        
        for i in range(numRows-1,-1,-1):
            print("row")
            print(i)
            print(first)
            print(second)
            
            start = numRows - 1 - i
            shift = 1
            current = start
            while current < size:
                print("current")
                print(current)
                print(s[current])
                str = str + s[current]
                if(second == 0):
                    current = current + first
                elif(first == 0):
                    current = current + second
                else:
                    if(shift):
                        current = current + first
                        shift = 0
                    else:
                        current = current + second
                        shift = 1

            first = first - 2
            second = second + 2        
        return str
               




        