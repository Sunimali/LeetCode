class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        first = 0
        last = 0
        size = len(s)
        dic = {}

        while(last!= size):
            if(s[last] not in dic):
                dic[s[last]] = True
            else:
                if dic[s[last]]:
                    #remove from front
                    while(s[first]!= s[last]):
                        dic[s[first]] = False
                        first = first + 1
                    first = first + 1 #remove

                else:
                    dic[s[last]] = True
             #calculate current len
            inter = last - first + 1
            if(inter > max_len):
                max_len = inter
            last = last + 1

        return max_len
                    





        