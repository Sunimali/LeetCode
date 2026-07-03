class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        if firstList is None or secondList is None:
            return []

        curFirst = 0
        curSec = 0
        ans = []

        while curFirst < len(firstList) and curSec < len(secondList):
            f = firstList[curFirst]
            s = secondList[curSec]

            if not((s[0] < f[0] and s[1] < f[0]) or (s[0] > f[1] and s[1] > f[1])):
                ans.append([ max(s[0], f[0]), min(s[1], f[1]) ])

            if s[1] > f[1]:
                curFirst  =  curFirst + 1
            elif s[1] < f[1]:
                curSec = curSec + 1
            else:
                curFirst  =  curFirst + 1
                curSec = curSec + 1
        return ans

