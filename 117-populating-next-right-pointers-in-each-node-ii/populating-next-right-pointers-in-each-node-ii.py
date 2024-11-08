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
            size = len(queue)  #get the node count in one level
            current = None
            prev = None 
            for i in range(size): #iterate through all noeds in level
                t = queue.popleft()
                current = t
                if prev is None: #initial one in level
                    prev = current
                else: #next ones
                    prev.next = current
                    prev = current
                if t is not None: # if t is empty ignore
                    if t.left: #only add to queue if it not null
                        queue.append(t.left)
                    if t.right:      
                        queue.append(t.right) 
                          
        return root                





        