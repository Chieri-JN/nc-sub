"""
given lst return all subsets, no dupes


can we sort input? this way we can simplify dup logic 
otherwise used seen set 

want to skip adding it if nums[i] == prev and not usedPrev

worse case if we cant use ordering we can use dict with flag saying weather it was used or not
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def backtrack(idx, currSS, usedPrev, prev):
            if idx == n:
                res.append(currSS)
            else:
                val = nums[idx]
                if idx == 0 or val != prev or (val == prev and usedPrev):
                    newSS = currSS + [val]

                    backtrack(idx+1, newSS, True, val)

                backtrack(idx+1, currSS, False, val)


        backtrack(0, [], False, None)


        return res


