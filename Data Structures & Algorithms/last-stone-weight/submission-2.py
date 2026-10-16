"""

"""
from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones)

        while len(stones) > 1:
            x = heappop_max(stones)
            y = heappop_max(stones)
            z = abs(x - y) 

            heappush_max(stones,z) if z else None


        return stones[0] if len(stones) else 0