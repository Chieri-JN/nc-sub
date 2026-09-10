"""
wnat to search rotated arr to find min

looking for valleys 

ex: using bin search: hi, lo -> look at neighbors
    - we want to find point where both neighbors are bigger 
    - when hi == lo
    
how to do hi, lo, mid 
    - look at neighbors of lo -> r, mid ->l,r and hi -> l
    - min will be where 
    - if any point has bigger n on bothsides its the min
    - wnat to find side that conflics 
         - mid : l,r on
[3,4,5,6,1,2]
mid = 5, lo = 3, hi = 2
 lo inc  dec mid inc  dec hi     

mid = 6, lo = 5, hi = 2
lo inc dec mid dec dec hi

[4,5,0,1,2,3]
 lo = 4, mid = 0, hi = 3
lo inc inc mid inc dec hi

[4,5,6,7]
lo = 4, mid = 5, hi = 7
lo inc dec mid inc dec hi


- if midL and midR < mid return midR 
- midRL, MidR > mid return mid
- if lo < hi, take lo, if hi < lo take hi

[3,4,5,6,1,2]
lo = 2, mid = 3, hi = 5
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n-1

        while lo < hi:
            mid = (lo + hi) // 2
            # print(f" nums[mid - 1]: { nums[mid-1]}, nums[mid]: {nums[mid]}, nums[(mid + 1) % n]: { nums[(mid + 1) % n]}")
            # print(f"lo:{lo}, mid: {mid}, hi:{hi}")
            # print(f"nums[lo]:{nums[lo]}, nums[mid]: {nums[mid]}, nums[hi]:{nums[hi]}")
            if nums[(mid + 1) % n] > nums[mid] and nums[(mid - 1)] > nums[mid]:
                return nums[mid]
            elif nums[(mid + 1) % n] < nums[mid] and nums[(mid - 1)] < nums[mid]:
                return nums[(mid + 1) % n]

            if nums[(lo + 1) % n] > nums[lo] and nums[(lo - 1)] > nums[lo]:
                return nums[lo]
            elif nums[(lo + 1) % n] < nums[lo] and nums[(lo - 1)] < nums[lo]:
                return nums[(lo + 1) % n]
            if nums[(hi + 1) % n] > nums[hi] and nums[(hi - 1)] > nums[hi]:
                return nums[hi]
            elif nums[(hi + 1) % n] < nums[hi] and nums[(hi - 1)] < nums[hi]:
                return nums[(hi + 1) % n]
            else: # dec mid inc
                if nums[mid] < nums[(lo)]:
                    hi = mid
                else:
                    lo = mid+1
        return nums[lo]
