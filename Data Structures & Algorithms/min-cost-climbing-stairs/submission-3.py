"""
dp[i] = min(dp[i-1] + cost[i-1], dp[i-2]+ cost[i-2])
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp1 = 0
        dp2 = 0

        for i in range(2, n):
            dp3 = min(dp1 + cost[i-1], dp2 + cost[i-2])

            dp2 = dp1
            dp1 = dp3
        
        return min(dp1 + cost[n-1], dp2 + cost[n-2])