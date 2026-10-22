class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        excludeFirst = nums[1:]
        excludeLast = nums[:-1]

        nxt1, skip1 = 0, 0 
        nxt2, skip2 = 0, 0 

        n = len(excludeLast)

        for i in range(n):
            tmp1 = max(excludeFirst[i] + skip1, nxt1)

            skip1 = nxt1
            nxt1 = tmp1

            tmp2 = max(excludeLast[i] + skip2, nxt2)

            skip2 = nxt2
            nxt2 = tmp2

        return max(nxt1, nxt2)