class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check if curr num is start of sequence 
        # if start of sequence count how long sequence is
        # return longest sequence
        numSet = set(nums)
        maxCount = 0
        for n in nums: 
            if n-1 not in numSet: 
                currCount = 1
                i = 1
                while (n+i in numSet): 
                    currCount += 1
                    i += 1
                if currCount > maxCount:
                    maxCount = currCount

        return maxCount

