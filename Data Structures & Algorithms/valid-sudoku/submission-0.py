"""
need to validate sudoku board

we need to go over each cell in the 9 x 9 grid

bf - O(1) if you tihnk about it its always 81 cells
bf space -> 27 sets 
    using 27 sets for rows, cols and 3x3 cells

for for each cell board[i][j] 
check if cell in rows[i]
in cols j
and sub[i,j] -> make helper function? crereate table cosntant 9,  

"""
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subs = defaultdict(set) 
        groups = {
            (0,0) : 0, (0,1): 1, (0,2): 2,
            (1,0) : 3, (1,1): 4, (1,2): 5,
            (2,0) : 6, (2,1): 7, (2,2): 8,
        }


        def getSB(i, j):
            return groups[(i // 3, j // 3)]


        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".": continue
                if val in rows[i] or  val in cols [j] or  val in subs[getSB(i,j)]:
                    return False
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    subs[getSB(i,j)].add(val)

        return True
