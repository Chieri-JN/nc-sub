"""
give a 2d grid of fresh and rotten fruit return how many minutes it takes to for all the fruit is rotten 
otherwise return -1

we can sue multi source bfs, but we have to stges, each frontier counts as a miniute 
    - if we get no more new frontiers then we have reached the end and we must 
    deterine if all the fruit is rotten (can keep set fo fresh fruit if its non empty thenr return -1)


1 edge case is that there are only rotten fruit (we dont want to get t = 1) return ealry
"""
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        moves = [(1,0), (-1, 0), (0,1), (0,-1)]
        q = deque()

        # fresh = set()
        freshCount = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    # fresh.add((i,j))
                    freshCount += 1
                elif grid[i][j] == 2:
                    q.append((i,j))

        # if there are no fresh fruits
        if freshCount == 0:
            return 0

        mins = 0
        while q:
            newQ = deque()
            for i,j in q:
                for dv, dh in moves:
                    newI, newJ = i + dv, j + dh
                    isValidI = 0 <= newI < n
                    isValidJ = 0 <= newJ < m
                    isValid = isValidI and isValidJ
                    if isValid and grid[newI][newJ] == 1:
                        freshCount -= 1
                        grid[newI][newJ] = 2
                        newQ.append((newI, newJ))
            q = newQ
            mins += 1

        return -1 if freshCount else mins-1

        
