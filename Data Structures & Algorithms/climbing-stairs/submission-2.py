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

space optimize
use n-1, n-2
dp[i] = dp[i-1] + dp[i-2]
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp1 = 1
        dp2 = 1
        for i in range(n):
            print(f"dp1: {dp1}")
            print(f"dp2: {dp2}")
            if i - 2 >= 0:
                dpi = dp1 + dp2
                dp2 = dp1 
                dp1 = dpi


        return dp1 + dp2