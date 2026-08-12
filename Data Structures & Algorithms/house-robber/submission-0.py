class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        n = len(nums)
        def topDown(i): 
            if i < 0:
                return 0
            else:
                pick = -1
                if i-2 in memo: 
                    pick = memo[i-2]
                else: 
                    pick =  topDown(i-2)
                    memo[i-2] = pick
                pick += nums[i]

                noPick = -1
                if i-1 in memo: 
                    noPick = memo[i-1]
                else: 
                    noPick =  topDown(i-1)
                    memo[i-1] = noPick
                hrI = max(pick, noPick)
                memo[i] = hrI
                return hrI

        return topDown(n-1)