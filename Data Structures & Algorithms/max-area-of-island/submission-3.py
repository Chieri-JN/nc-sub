"""
we can use ss bfs 
from current point we run bfs to get size of land , return size of island 
1s can not be connected diagonally 
track max
"""
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        n, m = len(grid), len(grid[0])

        def bfs(source):
            area = 1
            i, j = source
            q = deque()
            q.append((i,j))
            seen.add((i,j))

            while q:
                coordI, coordJ = q.popleft()
                for m1, m2 in moves:
                    newI, newJ = coordI + m1, coordJ + m2
                    isValidI =  newI < n and newI >= 0
                    isValidJ = newJ < m and newJ >= 0
                    valid = isValidI and isValidJ
                    if valid and grid[newI][newJ] and (newI, newJ) not in seen: 
                        area += 1
                        seen.add((newI, newJ))
                        q.append((newI, newJ))

            return area


        maxArea = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i,j) not in seen:
                    maxArea = max(maxArea, bfs((i,j)))


        return maxArea