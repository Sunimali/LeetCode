class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        size = len(citations)
        citations.sort() #sort the array
        curentH = 0 #keep current maximum value
        h = 0
        for i in range(size): #iterate through the citations
            diff = size - i #papers count which have atleast citations[i] citations count
            if(diff >= citations[i]):#if citations count is smaller or equal to papers count we take citations count
                currentH = citations[i]
            else:
                currentH = diff #else we takes the papers count
            if(currentH > h): #update the h value
                    h = currentH
        return h;            
        