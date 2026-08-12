class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        maxSize = 0
        visited = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        def explore(pos):
            currSize = 1
            visited.add(pos)
            q = deque()
            q.append(pos)

            while q:
                v,h = q.popleft()
                for d,k in dirs:
                    vd, hk = v+d, h+k
                    if 0 <= vd and vd < m and 0 <= hk and hk < n and grid[vd][hk]==1 and (vd,hk) not in visited:
                        visited.add((vd,hk))
                        q.append((vd,hk))
                        currSize += 1

            return currSize
            

        for i in range(m):
            # print("I: ", i)
            for j in range(n):
                # print("j: ", j)
                if (i,j) not in visited and grid[i][j] == 1:
                    # print("visiting")
                    cSize = explore((i,j))
                    # print(cSize)
                    maxSize = max(maxSize, cSize)
        

        return maxSize