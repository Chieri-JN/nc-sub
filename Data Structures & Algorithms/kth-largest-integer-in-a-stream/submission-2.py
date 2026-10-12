"""
easiest way to maintain is to maintain 2 heaps
1 with only k elems -> max heap
1 for overflow 

"""
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # nums.sort()
        # n = len(nums)
        # diff = n-k if n >= k else 0
        self.heapk = nums
        heapq.heapify(self.heapk)
        # self.overflow = nums[:diff]

    def add(self, val: int) -> int:
            heapq.heappush(self.heapk, val)

            while len(self.heapk) > self.k:
                heapq.heappop(self.heapk)
            kth = heapq.heappop(self.heapk)
            heapq.heappush(self.heapk, kth)

            return kth



