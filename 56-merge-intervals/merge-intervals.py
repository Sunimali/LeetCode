class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_intr = sorted(intervals, key = lambda item: item[0])   
        
        first = 0
        last = 1
        if not sorted_intr:
            return []
        if len(sorted_intr) == 1:
            return sorted_intr

        while last < len(sorted_intr):
            f_item = sorted_intr[first]
            l_item = sorted_intr[last]

            if f_item[1] >= l_item[0]:  # Overlap exists
                # Merge the intervals
                merged_item = [f_item[0], max(f_item[1], l_item[1])]
                sorted_intr[first] = merged_item
                # Remove the last interval since it's merged
                sorted_intr.pop(last)
            else:
                # No overlap
                first += 1
                last += 1

        return sorted_intr
      



            

            
        
        



        