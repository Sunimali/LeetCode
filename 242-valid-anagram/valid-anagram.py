class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = str(s)
        t = str(t)
        s.replace(" ","")
        t.replace(" ","")
     
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        