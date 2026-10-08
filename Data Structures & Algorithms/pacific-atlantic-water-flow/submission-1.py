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
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r, c = len(heights), len(heights[0]) 
        ocean = [[(None, None) for _ in range(c)] for _ in range(r)] # P, A
        moves = [(1,0), (-1,0), (0,1), (0,-1)]

        byP = lambda x: x[0] == 0 or x[1] == 0
        byA = lambda x: x[0] == r-1 or x[1] == c-1

        res = []

        def runBFS(i,j):
            seen = set()
            def dfs(a,b): 
                P, A = ocean[a][b][0] or byP((a,b)), ocean[a][b][1] or byA((a,b))
                lvl = heights[a][b]
                
                seen.add((a,b))

                for v, h in moves:
                    if P and A:
                        break
                    newA, newB = a + v, b + h
                    isValidA = 0 <= newA < r
                    isValidB = 0 <= newB < c
                    isValid = isValidA and isValidB
                    if  isValid:
                        newH = heights[newA][newB]
                        nP, nA = ocean[newA][newB]
                        if nP and nA and newH <= lvl:
                            P, A = nP, nA
                            continue
                        elif newH <= lvl and (newA, newB) not in seen:
                            seen.add((newA, newB))
                            dP, dA = dfs(newA, newB)
                            ocean[newA][newB] = (nP or dP, nA or dA)
                            P, A = P or ocean[newA][newB][0], A or ocean[newA][newB][1]
                        
                        
                if not P and not A:
                   P, A = False, False

                ocean[a][b] = (P, A)
                return (P, A)

            ocean[i][j] = dfs(i, j)

        for i in range(r):  
            for j in range(c):
                P, A = ocean[i][j] 
                if P and A:
                    res.append([i,j])
                elif P == False and A == False:
                    continue
                else:
                    runBFS(i,j)
                    P, A = ocean[i][j] 
                    if P and A:
                        res.append([i,j])

        return res


