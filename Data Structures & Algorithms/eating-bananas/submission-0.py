class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        minK, maxK = 1, max(piles)
        while minK != maxK:
            midK = (minK + maxK) // 2

            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / midK)

            # if hours == h:

            #     print("returning")
                # return midK
            if hours > h:
                minK = midK + 1
            else:
                maxK = midK

        return minK