class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split() #split by space
        size  = len(words)

        ans = words[size -1] #to intialize the string if use "" space will be at begining
        for i in range(size-1):
            ans = ans + " "+ words[size - 2 - i] # start from second last item
        return ans    

        