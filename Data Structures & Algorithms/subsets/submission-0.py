"""
all possible subsets, 
    - given ss we can either include num or not,

be careful of list aliasing
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def makeSS(idx, currSS):
            if idx == n:
                res.append(currSS)
            else:
                newSS = currSS + [nums[idx]]
                makeSS(idx+1, newSS)
                makeSS(idx+1, currSS)
        makeSS(0, [])

        return res
        
