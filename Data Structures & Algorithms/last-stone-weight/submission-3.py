"""

"""
from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapify(stones)

        while len(stones) > 1:
            x = heappop(stones)
            y = heappop(stones)
            z = (x - y)

            heappush(stones,z) if z else None


        return -stones[0] if len(stones) else 0