class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_new = ''.join(letter for letter in s if letter.isalnum()).lower()
        s_new_reversed = s_new[::-1]

        return s_new == s_new_reversed
        