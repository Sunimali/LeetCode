class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dic = {}
        split_s = s.split()
        len_s = len(split_s)

        len_pat = len(pattern)

        if(len_pat != len_s):
            print("f")
            return False
        else:
            for i in range(len_s):
                #check pat chatracter already in dictionary
                if pattern[i] in dic:
                    #check if it is equal to current s value
                    if dic[pattern[i]] != split_s[i]:
                        return False
                
                else:
                    #add to dictionary
                    if split_s[i] in dic.values():
                        return False
                    dic[pattern[i]] = split_s[i]
            return True



        