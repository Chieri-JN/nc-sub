"""
use set to keep track of whats in the list then look to see if theres anything greater
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxCnt = 0
        # for n in nums:
        while numSet:
            cnt = 1
            n =  numSet.pop()
            currIncr = n + 1
            currDecr = n - 1
            while currIncr in numSet or currDecr in numSet:
                if currIncr in numSet:
                    cnt += 1
                    numSet.remove(currIncr)
                    currIncr += 1
                if currDecr in numSet:
                    cnt += 1
                    numSet.remove(currDecr)
                    currDecr -= 1

            maxCnt = max(maxCnt, cnt)

        return maxCnt