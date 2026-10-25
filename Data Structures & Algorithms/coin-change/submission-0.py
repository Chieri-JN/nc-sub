"""
where i is the amount
dp[i] = 1 + min(dp[i-d]) where d is all the possible coin values 
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = amount + 1
        dp = [float("inf")] * n
        dp[0] = 0
        for i in range(n):
            for c in coins:
                if i + c < n:
                    dp[i+c] = min(dp[i+c], dp[i] + 1)

        # print(dp)
        return int(dp[n-1]) if dp[n-1] != float("inf") else -1