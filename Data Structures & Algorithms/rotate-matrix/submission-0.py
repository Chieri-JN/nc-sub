"""
rotate in place

ex:
1 (0,0) -> (0,1)
2 (0,1) -> (1,1)
3 (1,0) -> (0,0)
4 (1,1) -> (1,0)
n x n

update rule
new_row = col 
new_col = n - row - 1

how to do in place?
    - swaps? how do we perform, 
    - we could also do n swaps till we're done
        - i.e 1 takes 2s spot, then we take
    - keep count of swaps performed, 
    - so we have current position, and 
    - w 

algo: only gets corners/outer peram
    - count (while not == n*n)
    - currPosition
    - nextPosition
    - backup  # value previously at nextPosition
    - curr = next

# reverse than swap across diag (ignor diag values)
    - for i in range:
        
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        count = 0

        matrix.reverse() 

        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



        # currRow = 0
        # currCol = 0
        # currVal = matrix[0][0]
        # while count < n*n:
            
        #     nxtRow = currCol
        #     nxtCol = n - currRow - 1
        #     backup = matrix[nxtRow][nxtCol]
        #     fr = f"from ({currRow},{currCol})"
        #     to = f"moving {currVal} to ({nxtRow},{nxtCol}) "
        #     print(to + fr)

        #     matrix[nxtRow][nxtCol] = currVal

        #     currVal = backup
        #     currRow = nxtRow
        #     currCol = nxtCol
        #     count += 1




