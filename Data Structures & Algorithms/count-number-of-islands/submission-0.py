from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        count = 0
        # we can either go up/down left right (if only connect on diagonal its 
                #considered diff island)
        # def isValidPos((v,h)):
        #     return 0 <= v and v < m and 0 <= h and h < n and grid[v][h] == "1"

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def explore(pos):
            q = deque([])
            q.append(pos)
            visited.add(pos)
            while q:
                cPos = q.popleft()
                # print("cPos: ", cPos) 
                for v,h in dirs:  
                    newP = (cPos[0]+v, cPos[1]+h)
                    # print("("+str(v)+", "+str(h)+")")
                    # print("newP: ", newP)
                    if 0 <= newP[0] and newP[0] < m and 0 <= newP[1] and newP[1] < n and grid[newP[0]][newP[1]] == "1" and newP not in visited:
                   
                        visited.add(newP)
                        q.append(newP)
        


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    print("new Island at : ", (i,j))
                    count += 1
                    explore((i,j))

        return count