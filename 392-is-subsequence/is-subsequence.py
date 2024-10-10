class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        size = len(t)
        start = 0
        for i in s:
            t = t[start:size]
            j = t.find(i)
            if(j==-1):
                return False
            else:
                start = j+1
        return True            
            

        