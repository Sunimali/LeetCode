class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        #build the graph

        p = len(prerequisites)
        graph = {}

        for i in range(p):
            c1 = prerequisites[i][0] #first course
            c2 = prerequisites[i][1] #second course
            if c2 not in graph:
                graph[c2] = []
            graph[c2].append(c1)
 
        #traverse dfs graph and find cycles exsist or not
        for node in graph:
            visited =  [False] *numCourses
            rec_stack = [False] *numCourses
            ans = self.dfs_search(graph, node,visited,rec_stack)
            if not ans:
                return False #cycle exist
        return True   #no cycle     

    def dfs_search(self,graph,node,visited,rec_stack):
        visited[node] = True
        rec_stack[node] = True
        neighbours =  []
        if node in graph:
            neighbours = graph[node]
        for n in neighbours:
            if not visited[n]:
                ans = self.dfs_search(graph,n,visited,rec_stack)
                if not ans:
                    return False #cycle exsist
            elif  rec_stack[n]:
                return False  #cycle exsist
        rec_stack[node] = False        
        return True #no cycle            


        


        