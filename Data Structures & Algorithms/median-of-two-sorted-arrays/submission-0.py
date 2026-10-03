"""
we want to construct the left partition

using shortests list, find midle, and compare it it to half - im of second list(where the mideab wiuld live)
if aLeft < bleft and Aright < bRight, we ahve median is min (Arigt, bLeft)
if not, 

"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)


        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2
        while True: # guarenteed median
            midA = (l + r) // 2
            midB = half - midA - 2

            aL = A[midA] if midA >= 0 else float("-inf")
            aR = A[midA + 1] if midA < (len(A) - 1) else float("inf")

            bL = B[midB] if midB >= 0 else float("-inf")
            bR = B[midB + 1] if midB  < (len(B) - 1) else float("inf")

            if aL <= bR and bL <= aR:
                if total % 2: 
                    return min(bR, aR)
                return (max(bL, aL) + min(aR, bR)) / 2

            if aL > bR:
                r = midA - 1
            else:
                l = midA + 1

