
class Solution:
    import bisect
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        indexes = []
        eds = []
        answer = []
    
        for i, p in enumerate(points):
            ed = p[0]** 2 + p[1]** 2
            pos = bisect.bisect_left(eds, ed)

            indexes.insert(pos, i)
            eds.insert(pos,ed)
        
        for i in range(k) :
            answer.append(points[indexes[i]])

        return answer


            