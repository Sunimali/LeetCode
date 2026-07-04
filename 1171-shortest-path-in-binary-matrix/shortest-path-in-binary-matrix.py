from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
      
        start_row = 0
        start_cl = 0
        q = deque([[start_row, start_cl ]])
        visited = {(start_row, start_cl )}
        distance = {(start_row, start_cl ): 1}

        if grid[0][0] != 0 or  grid[len(grid) - 1][len(grid) - 1] !=0: #no clear path
            return -1
        while q:

            cell = q.popleft()
            r = cell[0]
            c = cell[1]

            if r+1 < len(grid):
                if (r+1, c) not in visited:
                    visited.add((r+1, c))
                    if grid[r+1][ c] == 0:
                        distance[(r+1, c)] = distance[(r, c)] + 1
                        q.append([r+1, c])
            if c+1 < len(grid):
                if (r, c+1) not in visited:
                    visited.add((r, c+1))
                    if grid[r] [c+1] == 0:
                        distance[(r, c+1)] = distance[(r, c)] + 1
                        q.append([r, c+1])
            if r+1 < len(grid) and  c+1 < len(grid):
                if (r+1, c+1) not in visited:
                    visited.add((r+1, c+1))
                    if grid[r+1][ c+1] == 0:
                        distance[(r+1, c+1)] = distance[(r, c)] + 1
                        q.append([r+1, c+1])
            if (r-1) >= 0:
                if (r-1, c) not in visited:
                    visited.add((r-1, c))
                    if grid[r-1][ c] == 0:
                        distance[(r-1, c)] = distance[(r, c)] + 1
                        q.append([r-1, c])
            if (c-1)  >= 0:
                if (r, c-1) not in visited:
                    visited.add((r, c-1))
                    if grid[r][ c-1] == 0:
                        distance[(r, c-1)] = distance[(r, c)] + 1
                        q.append([r, c-1])
            if (r-1) >= 0 and  (c-1) >= 0:
                if (r-1, c-1) not in visited:
                    visited.add((r-1, c-1))
                    if grid[r-1][ c-1] == 0:
                        distance[(r-1, c-1)] = distance[(r, c)] + 1
                        q.append([r-1, c-1])
        
            if (r-1) >= 0 and  c+1 < len(grid):
                if (r-1, c+1) not in visited:
                    visited.add((r-1, c+1))
                    if grid[r-1][ c+1] == 0:
                        distance[(r-1, c+1)] = distance[(r, c)] + 1
                        q.append([r-1, c+1])
            if r+1 < len(grid) and  (c-1) >= 0:
                if (r+1, c-1) not in visited:
                    visited.add((r+1, c-1))
                    if grid[r+1][ c-1] ==0:
                        distance[(r+1, c-1)] = distance[(r, c)] + 1
                        q.append([r+1, c-1])

        if (len(grid) - 1, len(grid) - 1) in distance:
            return distance[(len(grid) - 1, len(grid) - 1)]
        else:
            return -1
                

                    
                    
                        




