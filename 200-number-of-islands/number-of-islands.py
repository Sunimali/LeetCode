class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        current = 2
        if grid is None:
            return 0
        r = len(grid)
        c = len(grid[0])

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '0': #water
                    continue
                elif(grid[i][j] == '1'): #land
                    self.traverse(grid, current, i, j, r, c)
                    current = current + 1
        return current - 2               



    def traverse(self, grid, current, i, j, r, c):
        if grid[i][j] != '1': #water
            return
            
        grid[i][j] = current
        
        if i > 0:
            self.traverse(grid, current, i - 1, j, r, c)
        if i < r - 1:    
            self.traverse(grid, current, i + 1, j, r, c)
        if j > 0:    
            self.traverse(grid, current, i , j - 1, r, c)
        if j < c - 1:    
            self.traverse(grid, current, i , j + 1, r, c)

        