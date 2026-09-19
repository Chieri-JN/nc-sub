"""
for dp[i] =
    - if dp i == true: 
        for all spots reachable from i, mark as true
    - else do nothing
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n

        for i in range(n):
            if i == 0:
                dp[i] = True
            if dp[i]:
                for j in range(1, nums[i] + 1):
                    if i + j < n:
                        dp[i + j] = True
    
        return dp[n-1]