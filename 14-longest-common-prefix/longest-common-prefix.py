class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if strs is None:
            return ""
        if len(strs) == 1:
            return strs[0]

        min_index = min(range(len(strs)), key = lambda i: len(strs[i]))
        small = strs[min_index]
        prefix = []

        for i, s in enumerate(small):
            exists = False
            for j, st in enumerate(strs) :
                
                if j == min_index:
                    continue
                if st[i] == s: #prefix
                    exists = True
                else:
                    exists = False
                    break
            if exists:
                prefix.append(s)
            else:
                break
            
        
        
        return "".join(prefix)



