from collections import deque
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = deque()
        dupfound = False

        for c  in s:
            if stack:
                if stack[-1] == c:
                    dupfound = True
                    stack.pop()
                else:
                    stack.append(c) 

            else:
                stack.append(c)
        
        return "".join(stack)
        
        