"""
unique asnwe whcih means we wont have two points equi-dsitance w/ k == 1
"""
from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distances = []

        for i, (x,y) in enumerate(points):
            xSqr = (0 - x) ** 2
            ySqr = (0 - y) ** 2
            d = math.sqrt(xSqr + ySqr)
            points[i] = [d, x, y]

        heapify(points)
        
        res = []
        for i in range(k):
            d, x, y = heappop(points)
            res.append([x,y])


        return res
