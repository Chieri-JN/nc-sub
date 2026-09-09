"""
gievn list of piles where piles[i] is the number of banaas in that pile
we are also given h, the number of hours we have to eat all the banas. The goal is to find the min
k such that we can eat all the banaas in h/ 

Constraits: 
    - must eat all banas in h hours
    - 

inital ideas / human: 
    - pick a k that already exists within the pile 
        - we start with the biggest k and smallest k, if it works we use "bin search" to find
        - we then cehck that k against the nums 
    - runtime O(nlogn) [sort] + O(nlogn) logn search * O(n) for check 

    - condition, if tmpH > h, then we need to find a bigger k ,
    - if tmpH <= h we will try to find a smaller k

"""
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        k = float("inf")
        lo, hi = 1, max(piles)

        while lo <= hi:
            mid = (lo + hi) // 2
            tmpK = mid
            tmpH = 0
            for p in piles:
                tmpH += math.ceil(p / tmpK)
                if tmpH > h:
                    break
            if tmpH > h:
                lo = mid + 1
            else: 
                k = min(k, tmpK)
                hi = mid 
                if hi == lo:
                    break

        return k