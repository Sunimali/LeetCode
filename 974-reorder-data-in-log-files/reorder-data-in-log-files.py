class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        ans = []
        digit_log = []
        letter_log = []

        for index, log in enumerate(logs):
            tokens = log.split(" ")
           
            if tokens[1].isdigit(): #numerical log
                digit_log.append(log)
            else:
                letter_log.append((index, tokens[0], tokens[1:len(tokens)] ))
            
        letter_log.sort(key = lambda x:( x[2], x[1]))
        
        for  item in letter_log:
            ans.append(logs[item[0]])
        ans = ans + digit_log
        return ans




        