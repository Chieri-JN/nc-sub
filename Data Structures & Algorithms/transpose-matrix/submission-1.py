class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        new_matrix = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                
                new_matrix[i][j] = matrix[j][i]


        return new_matrix