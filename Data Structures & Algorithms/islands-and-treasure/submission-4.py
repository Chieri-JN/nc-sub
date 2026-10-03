"""
we can use bfs from each treasure cell, if we hit a land cell the dist is the min of the current dis and
the new dist

why bfs instead of dfs? 
    - bfs gives us shortest dist whereas dfs will find a dist (not necessarily shortest)

caveats/ things to watch out for:
    - we dont want to get stuck in inf loop so we need seen set, for each bfs pass 
    - why not global? we dont know if current treasrue source is the closest
        - maybe we could use global but management is trickign
    - 

"""
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        seen = set()
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                   q.append((i, j, 1))
        
        while q: 
            i, j, d = q.popleft()
            for v, h in moves:
                newI, newJ = i + v, j + h
                isValidI = 0 <= newI < m
                isValidJ = 0 <= newJ < n
                isValid = isValidI and isValidJ and (newI, newJ) not in seen
                if isValid and grid[newI][newJ] > 0 and d < grid[newI][newJ]:
                    grid[newI][newJ] = min(grid[newI][newJ], d) 
                    seen.add((newI, newJ))
                    q.append((newI, newJ, d+1))
            
        
      

