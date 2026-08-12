class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * m for i in range(n)]
        maxArea = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0":
                    continue
                else:
                    up, left, diag = 0, 0, 0
                    if j > 0:
                        left = dp[i][j - 1]
                    if i > 0:
                        up = dp[i - 1][j]
                    if i > 0 and j > 0:
                        diag = dp[i - 1][j - 1]
                    dp[i][j] = min(up, left, diag) + 1
                    maxArea = max(maxArea, dp[i][j])
        return maxArea * maxArea
