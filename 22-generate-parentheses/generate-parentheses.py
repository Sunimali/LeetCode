class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        current = ['()']
        current = self.rec_pranthesis( 2, current, n)
        return current
     
    def rec_pranthesis(self, itr, current, n):
        next_list = []
        if itr > n: 
            return current
        else:
            for item in current:
                for p in range(len(item)):
                    if(item[p]=='('):
                        new_item = item[0:p+1]+ '()'+ item[p+1:len(item)]
                        if new_item not in next_list:
                            next_list.append(new_item)
                
                next_list.append(item+'()')
            return self.rec_pranthesis( itr+1, next_list,n)
                        

                


        

        