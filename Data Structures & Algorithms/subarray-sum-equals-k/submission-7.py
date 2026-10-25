"""
can use backtracking to construct subarrays

fro each number we can either include it or not 

only include it if addign it doesnt increase curr sum past k, (also allows early stop since we sort)
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = currSum = 0
        preSums = {0 : 1}
        for num in nums:
            currSum += num
            diff = currSum - k

            count += preSums.get(diff, 0)
            preSums[currSum] = 1 + preSums.get(currSum, 0)

        return count




            
