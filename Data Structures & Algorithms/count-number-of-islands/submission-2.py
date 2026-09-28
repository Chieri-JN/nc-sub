"""
count number of islands 

use bfs from source to find island bounds
use seen set for each seen coord
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        moves = [(1,0), (0,1), (0,-1), (-1,0)]
        seen = set()
        def bfs(source):
            i,j = source
            seen.add((i, j))
            for m1, m2 in moves:
                newI, newJ = i + m1, j + m2 
                validI = (newI < n and newI >= 0)
                validJ = (newJ < m and newJ >= 0)
                if validI and validJ:
                    if (newI, newJ) not in seen and grid[newI][newJ] == "1":
                        bfs((newI, newJ))

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in seen: 
                    bfs((i,j))
                    count += 1

        return count

                