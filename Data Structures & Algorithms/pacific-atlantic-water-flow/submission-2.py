"""
given isldant represented as matrix of heights, above sea level 

we want to return list of all cells from which water can flow to both P and A oceans 
    - (this means if we put) water on the cell, is there a path from it to both oceans 
        - that is monotonically decreasing (i.e from og cell ocean, h[c_i] >= h[c_i+1])

bf would be to just perform bfs from each cell
    - instead we dont need to revist every cell, we know that if exists path from v to X ocean 
        containing v-w-x-y-z then we know there is a pth to X ocean for all of w, x,y,z. 

Then at each cell we only need to check:
    - there is. apath to A ocean from its neighbors and that what can flow to neighbor

perform bfs for shortest path
algo:   
    - keep map of cell to ocean reach (also acts as seen)
    - check if A and P can be reached  on valid neighbors, else recursive bfs,
    - each node returns its oceanValue after its N returns

"""

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        r, c = len(heights), len(heights[0])
        ocean = [[None for _ in range(c)] for _ in range(r)]  # None = unresolved, else (P, A)
        moves = [(1,0), (-1,0), (0,1), (0,-1)]

        byP = lambda a, b: a == 0 or b == 0
        byA = lambda a, b: a == r-1 or b == c-1

        res = []

        def resolve(i, j):
            lvl = heights[i][j]
            component = [(i, j)]
            inComponent = {(i, j)}
            lowerNeighbors = []
            P, A = False, False

            # Step 1: flood-fill the whole equal-height plateau (cycle-safe, no memo needed here)
            stack = [(i, j)]
            while stack:
                a, b = stack.pop()
                if byP(a, b): P = True
                if byA(a, b): A = True
                for da, db in moves:
                    na, nb = a + da, b + db
                    if 0 <= na < r and 0 <= nb < c:
                        nh = heights[na][nb]
                        if nh == lvl and (na, nb) not in inComponent:
                            inComponent.add((na, nb))
                            component.append((na, nb))
                            stack.append((na, nb))
                        elif nh < lvl:
                            lowerNeighbors.append((na, nb))

            # Step 2: strictly-lower edges form a DAG -> safe to recurse/memoize normally
            for (na, nb) in lowerNeighbors:
                if P and A:
                    break
                if ocean[na][nb] is None:
                    resolve(na, nb)
                nP, nA = ocean[na][nb]
                P, A = P or nP, A or nA

            # Step 3: finalize the ENTIRE plateau at once -- no cell cached before this point
            for (a, b) in component:
                ocean[a][b] = (P, A)

        for i in range(r):
            for j in range(c):
                if ocean[i][j] is None:
                    resolve(i, j)
                P, A = ocean[i][j]
                if P and A:
                    res.append([i, j])

        return res


