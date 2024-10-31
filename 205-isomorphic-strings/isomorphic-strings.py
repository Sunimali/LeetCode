class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        replaced = {} #initilaize dictionary
        mappedt = {}
        for i in range(len(s)): #iterate through s and t
            if s[i] in replaced: #already in hastable
                if replaced[s[i]] != t[i]: #found unmatched mapping
                    return False
            else: #not in hashtable
                if(t[i] in mappedt): # No two characters may map to the same character(handling)
                    return False
                else:    
                    replaced[s[i]] = t[i] # add to hash table
                    mappedt[t[i]] = s[i]
        return True #no unmacthing pair found






        