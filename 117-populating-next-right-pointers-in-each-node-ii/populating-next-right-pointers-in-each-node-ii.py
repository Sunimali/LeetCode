"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        queue = deque()
        queue.append(root)


        while queue: #while is not empty

            size = len(queue)
            current = None
            prev = None

            print(size)
 
            for i in range(size):
                t = queue.popleft()
                current = t

                if prev is None:
                    prev = current
                else:
                    prev.next = current
                    prev = current

                if t is not None:
                    if t.left:
                        queue.append(t.left)
                    if t.right:      
                        queue.append(t.right) 
                          
        return root                





        