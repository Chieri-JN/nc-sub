class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def topDown(i):
            if i == 0 or i == 1:
                return cost[i]
            if i == n:
                return min(topDown(i-1), topDown(i-2))
            if i in memo:
                return memo[i]
            ic =  cost[i] + min(topDown(i-1), topDown(i-2)) 
            memo[i] = ic
            return ic

        return topDown(n)