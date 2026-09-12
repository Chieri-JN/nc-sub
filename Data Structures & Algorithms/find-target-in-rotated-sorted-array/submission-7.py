"""
perform binary search on rotated sorted array

one side may not be continuous 
 --> if mid < hi, and target > mid, check right 
 --> if mid > lo, and targt < mid, check left

---> non continous: if hi < mid
    -> if target > mid, and target > hi, check right
    -> else left
---> non continous: if lo > mid
    -> if target < mid and t < lo: check left
    else: right
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (hi + lo) // 2
            if nums[mid] == target:
                return mid
            else: 
                if nums[mid] < target:
                    if target <= nums[hi] or nums[hi] < nums[mid]:
                        lo = mid +1
                    else: 
                        hi = mid
                elif nums[mid] > target: 
                    if target >= nums[lo] or nums[lo] > nums[mid]:
                        hi = mid
                    else:
                        lo = mid + 1
               
        return -1 if nums[lo] != target else lo

                