class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split() #spilt by space
        size = len(words)

        lastword = words[size-1] #get the last word
        ans = len(lastword)
        return ans
        