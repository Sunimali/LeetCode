class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        para_stack = []
        open_brac = ['[','{','(']
        close_brac = [']','}',')']


        for i in s:
            if i in open_brac: #if it a open bracket put it into stack
                para_stack.append(i)
            else: #close bracket then pop the most recent open bracket
                if(len(para_stack)==0): #there is any closing bracket
                    return False
                else:    
                    open_recent = para_stack.pop()
                    open_index =  open_brac.index(open_recent) #find open bracket type
                    close_index = close_brac.index(i) #find closed bracked type

                    if(open_index == close_index): #open and closed pair matched correctly
                        continue
                    else:
                        return False 
        if(len(para_stack)==0):  #these should not any remain para in stack             
            return True
        else:
            return False    




        