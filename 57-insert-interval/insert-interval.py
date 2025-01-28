class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        size = len(intervals)
        new_intervals = []

        no_merge = True

        for i in range(size):

            interval = intervals[i]

            #whole inteverl is leftside of new interval then add to newlist
            if interval[1] < newInterval[0]:
                new_intervals.append(interval)
                continue

            #whole interval is in rightside of new interval then add to new list
            if interval[0] > newInterval[1]: 
                if no_merge:
                    new_intervals.append(newInterval)#add current new interval to newlist
                new_intervals.append(interval)
                no_merge = False
                continue

            #overlapped with new_interval

            newInterval[0] = min(interval[0],newInterval[0])
            newInterval[1] = max(interval[1],newInterval[1])

        if no_merge:
            new_intervals.append(newInterval)

        return new_intervals


            
                

            
        