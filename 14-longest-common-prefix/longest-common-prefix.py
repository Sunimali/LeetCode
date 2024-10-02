class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        strs.sort(key=len) #sort by the length
        shortword = strs[0] #get the minimum length word
        swsize = len(shortword)
        ps = swsize
        for i in strs: #iterate through all words
            if ps <0:
                break
            for j in range(ps): #iterate through possible prefix
                if i[j] != shortword[j]:
                    ps = j  #update the prefix length
                    break #move to next word
        if ps == 0:
            return ""
        else:
            return shortword[:ps]  #return longeth prefix



        