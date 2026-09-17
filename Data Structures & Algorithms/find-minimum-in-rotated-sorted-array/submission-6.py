"""
find min in rotated sorted List

use modified bin search 

- insights: 
    - since its incr we know that mid < r unless there is break
    - so we check mid 
        if mid > hi, we check r, 
        if else we check l
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]