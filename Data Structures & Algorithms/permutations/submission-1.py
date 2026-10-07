"""
gennerate all permuations of  a set of numbers

for each position add all available digits to end (track which ones are not used)

not so space efficient 
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        usedSet = [False] * n

        def makePerm(idx, currPerm, used):
            if idx == n:
                res.append(currPerm.copy())
            else:
                for i, digit in enumerate(nums):
                    if used[i]:
                        continue
                    
                    currPerm.append(digit)
                    used[i] = True
                    makePerm(idx + 1, currPerm, used)
                    used[i] = False
                    currPerm.pop()

        makePerm(0, [], usedSet)

        return res