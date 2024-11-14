class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        'O'
        if board is None:
            return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                else: #is O
                    #invalide O
                    if i == 0 or j == 0 or i == m - 1 or j == n-1: 

                        # board[i][j] = 'I' #INVALID
                        self.backtrack(board,i,j,m,n)

                        #backtrack the neighbours valid ones
                    elif(board[i-1][j]=='I' or board[i+1][j]=='I' or board[i][j+1]=='I' or board[i][j-1]=='I'):
                        # board[i][j] = 'I' #INVALID 
                        self.backtrack(board,i,j,m,n)        
                    else:
                        board[i][j] = 'V' #VALID
        #after choosing invalide and valid one iterate again through the list and change valid one to x and invalide one to o 

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'I':
                    board[i][j] = 'O'
                if board[i][j] == 'V':
                    board[i][j] = 'X'    
                
    def backtrack(self,board,i,j,m,n):
        if board[i][j] == 'I' or board[i][j] == 'X':
            return
        if board[i][j] == 'O' or board[i][j] == 'V':  
            board[i][j] = 'I' 
        if i >0:
            self.backtrack(board,i-1,j,m,n)
        if i < m -1 : 
            self.backtrack(board,i+1,j,m,n)
        if j >0:    
            self.backtrack(board,i,j-1,m,n)
        if j < n -1 :   
            self.backtrack(board,i,j+1,m,n)



        
            





        