"""
nened to search a sorted 2d matrict

two step bin search ->m first find correct row then search row 


algo: 
look at rows 
if num in between row start end then look within rrow
    -> normal bin search
if target is lss than row start --> move top
if target greater than row end 0---> move bootm 


matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
bot = 0, top = 3
mR = 1
[10,11,12,13]
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        bottom, top = 0, m
        lo, hi = 0, n

        # first find correct row
        while bottom < top: 
            midRow = (bottom + top) // 2
            # print(f"midRow: {midRow}")
            if target > matrix[midRow][n - 1]:
                bottom = midRow + 1
            elif target < matrix[midRow][0]:
                top = midRow
            else: # perform bin search on row
                
                while lo < hi:
                    mid = (lo + hi) // 2
                    # print(f"mid: {mid}")
                    if target == matrix[midRow][mid]:
                        return True
                    elif target > matrix[midRow][mid]:
                        lo = mid + 1
                    else:
                        hi = mid
                break

        return False