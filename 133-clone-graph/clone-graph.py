"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node is None:
            return None
        
        q = deque()
        visited = set()
        q.append(node)
        dic = {}
        head = None
    
        while q:
            n = q.pop()
            clone = None
            
            if n in visited:
                continue
            else:
                if n.val not in dic:
                    clone = Node(n.val, None)
                    dic[n.val] = clone
            
                visited.add(n)
            clone = dic[n.val]
            if head is None:
                head = clone

            c_n = []
            for n_i in n.neighbors:
                if n_i.val in dic:
                    c_n.append(dic[n_i.val])
                else:
                    clone_n = Node(n_i.val, None)
                    dic[n_i.val] = clone_n
                    c_n.append(clone_n)
                q.append(n_i)
            clone.neighbors = c_n
        return head
            
            
            


            
        