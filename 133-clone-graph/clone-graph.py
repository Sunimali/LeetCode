"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        c = None
        visited = set()
        older_map = {}
        
        c = self.dfs(node,c,visited, older_map)
        return c
    def dfs(self,node,c, visited, older_map ):

        if node is None:
            return c
       
        if node in older_map:
            return older_map[node]
        else:
            clone = Node(node.val)
            older_map[node] = clone
   
            for n in node.neighbors:
                clone.neighbors.append(self.dfs(n, c, visited, older_map ))
            
            return clone
        


        
              
        

        