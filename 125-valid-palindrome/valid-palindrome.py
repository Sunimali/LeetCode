from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:

        secstring = ""
        stackstring = ""
        stack = deque()

        for i in s:
            if i.isalnum():
                i_lower = i.lower()
                secstring += i_lower
                stack.append(i_lower) 
        while stack:
            stackstring+= stack.pop()
        return stackstring == secstring
        