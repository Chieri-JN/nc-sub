"""
gennerate all permuations of  a set of numbers

for each position add all available digits to end (track which ones are not used)

not so space efficient 
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def makePerm(idx, currPerm, used):
            if idx == n:
                res.append(currPerm.copy())
            else:
                for digit in nums:
                    if digit in used:
                        continue
                    
                    currPerm.append(digit)
                    freshUsed = used.copy()
                    freshUsed.add(digit)
                    makePerm(idx + 1, currPerm, freshUsed)

                    currPerm.pop()

        makePerm(0, [], set())

        return res