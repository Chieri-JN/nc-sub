"""
given n stairs, you want to return the number of ways you can reach the top

insight:
    - at each step we want to count how many ways it took to reach that step (bottom up)

    - from step n, we want to say we can reach steps n-1, and n-2
dp[i] = 
    - if i == n: dp[i] + dp[i]
    - else: dp[i+1] += dp[i], dp[i+2] += dp[i], dp

n = 2

[0,1,]

[1,1,2,1]
0- 1,2
1 - 1,2
2, - 1
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(n+1):
            if i + 1 <= n:
                dp[i + 1] += dp[i]
            if i + 2 <= n: 
                dp[i + 2] += dp[i]

        print(dp)
        return dp[n]