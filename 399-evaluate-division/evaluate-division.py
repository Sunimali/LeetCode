class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        e = len(equations)
        graph = {}
        ans = []

        #buid the grapgh
        for i in range(e):
            x = equations[i][0]
            x = str(x)
            y = equations[i][1]
            y = str(y)

            #check if x and y are in already grapgh or not
            if x not in  graph:
                graph[x] = {}
            graph[x][y] = values[i]

            if y not in graph:
                graph[y] = {}
            graph[y][x] = 1/values[i]
        print(graph)    
        #now lets go through the queries
        q = len(queries)
        for i in range(q):
            x = str(queries[i][0])
            y = str(queries[i][1])
            if x not in graph or y not in graph:
                ans.append(-1.0)
                continue
            val = 1
            visited = set()
            val = self.dfs(graph,x,y,val,visited)
            ans.append(val)
        return ans

     #get the x and do the dfs traverse until find find y
    def dfs(self,graph,x,y,val,visited):
        visited.add(x)
        if x == y:
            return val
        else:
            #get the unvisted node
            for n in graph[x]:
                if n not in visited:
                    new_val = val * graph[x][n]
                    res = self.dfs(graph,n,y,new_val,visited)
                    if res != -1.0:
                        return res
        return -1.0               
            
                

        























             
         






        