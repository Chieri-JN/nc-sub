"""
at each house we can choose to rob it or skip it we want ot max
amount money we can rob without alerting the police (i.e robbing adject houses)

recursive: 
    dp[i] = max
        - nums[i] + dp[i+2]
        - dp[i]

since we are maximizing there is no case we where we skip 2 houses


tabulation top down: 
    - start at house n, dp[i] = max of choosing curr house + skip or neighbor (dp[i+1])
    - dp[i]

tabulation bottom up: 
    - start at house 0, dp[i] = max of curr + skip or neighbor

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return nums[0]

        skip, nxt = 0, 0

        for i in range(n):
            tp = max(nums[i] + skip, nxt)
            skip = nxt
            nxt = tp


        return nxt


        
            

