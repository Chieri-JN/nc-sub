"""
spiral traversal of matrix

keep hor start end, and vert start end
currV and curr h and just iterate until we we've seen mxn things (or start == end)

use moveDir % 4 to encode move direction: 
    - 0 move left to right (incr vStart)
    - 1 move down
    - 2 move righ to left (decr vStart)
    - 3 move up 
use moveDir % 2 to decide if we move vertically or hor: 
after each iteration we flip start and end, start becomes end, end becomes start + 1

left vs right start  = 1 - moveDir % 3 (0 or 2)
down vs up start  = 2 - moveDir % 4 (1 or 3)


hS, hE = 0, 2 (iter 1, left to right) swawp, 
hS, hE = 2, -1 (iter 2, r to l)

"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        vStart, vEnd = 0, m-1
        hStart, hEnd = 0, n-1

        res = []
        # seen = set()
        moveDir = 0 # % %

        while len(res) < m * n:
            if moveDir % 2: 
                # odd so vertocal movement
                sign = 2 - (moveDir % 4)
                # print(f"vStart, vEnd, sign: {vStart}, {vEnd}, {sign}")
                for i in range(vStart, vEnd+sign, sign):
                    v = matrix[i][hStart]
                    res.append(v)
                vStart, vEnd = vEnd, vStart
                hStart += -sign

            else:
                # even so horizontal movement
                sign = 1 - (moveDir % 4)
                # print(f"hStart, hEnd, sign: {hStart}, {hEnd}, {sign}")
                for j in range(hStart, hEnd+sign, sign):
                    v = matrix[vStart][j]
                    res.append(v)
                
                hStart, hEnd = hEnd, hStart
                vStart += sign
                

            moveDir += 1


        return res
