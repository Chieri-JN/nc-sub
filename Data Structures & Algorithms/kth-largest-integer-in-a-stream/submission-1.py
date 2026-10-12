"""
easiest way to maintain is to maintain 2 heaps
1 with only k elems -> max heap
1 for overflow 

"""
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        n = len(nums)
        diff = n-k if n >= k else 0
        self.heapk = nums[diff:]
        heapq.heapify(self.heapk)
        self.overflow = nums[:diff]

    def add(self, val: int) -> int:
        # heapushpop_max
            # print(f"heap before adding {val}: {self.heapk}")
            excess = heapq.heappush(self.heapk, val)
            # print(f"heap after adding {val}:: {self.heapk}")
            while len(self.heapk) > self.k:
                heapq.heappop(self.heapk)
            kth = heapq.heappop(self.heapk)
            heapq.heappush(self.heapk, kth)
            # assert(len(self.heapk) == self.k)
            return kth
            # cnt = 1
            # rem = []
            # while cnt != self.k:
            #     rem.append(heapq.heappop(self.heapk))


