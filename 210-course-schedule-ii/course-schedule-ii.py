class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegrees = {}
        graph = {}
        ans = []
        req = len(prerequisites)
        if req == 0: #if there is no pre required order then can do anyway
            ans.extend(range(numCourses))
            return ans

        #build the graph
        for i in range(req):
            c1 = prerequisites[i][0] #need to do c2 first before c1
            c2 = prerequisites[i][1]

            if c2 not in graph:
                graph[c2] = []
            if c1 not in  graph:
                graph[c1] = []
            if c1 not in indegrees:    
                indegrees[c1] = 0
            if c2 not in indegrees:
                indegrees[c2] = 0    
            indegrees[c1] = indegrees[c1] + 1
            graph[c2].append(c1)
        if len(graph) < numCourses:
            for i in range(numCourses):
                if i not in graph:
                    ans.append(i)

        if not indegrees: #empty
            return ans

        for i in range(numCourses):
            current = self.find_indegree(indegrees)
            if current == -1:
                break
            else:
                ans.append(current)
                del indegrees[current]
                #decrement indegree value from neighbours of key(outgoing)
                neighbours = graph[current]
                for n in neighbours:
                    indegrees[n] = indegrees[n] - 1
        if len(ans) == numCourses:
            return ans
        else:
            return []

    def find_indegree(self, indegrees):
        for key,val in indegrees.items():
            if val == 0:
                return key
        return -1



            

        