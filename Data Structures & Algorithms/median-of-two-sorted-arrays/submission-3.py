"""
want to construct the left partition of the combo of both arrays

need to use bin search on first list to find split that is completly less than B



"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        lo, hi = 0, len(A)-1

        total = len(A) + len(B)
        half = total // 2
        while True:
            aMid = (lo + hi) // 2
            bMid = half - aMid - 2

            aLow = A[aMid] if len(A) > aMid >= 0 else float("-inf")
            aHi = A[aMid + 1] if aMid + 1 < len(A) else float("inf")

            bLow = B[bMid] if len(B) > bMid >= 0 else float("-inf")
            bHi = B[bMid + 1] if bMid + 1 < len(B) else float("inf")

            if aLow <= bHi and bLow <= aHi:
                if total % 2:
                    return min(aHi, bHi)
                else:
                    return (max(aLow, bLow) + min(aHi, bHi)) / 2

            if aLow > bHi:
                hi = aMid - 1
            else:
                lo = aMid + 1
