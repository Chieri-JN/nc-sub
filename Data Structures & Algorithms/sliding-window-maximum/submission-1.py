"""
given list and num k where k is window size, want to return list 
max nums in window (at each stage)

brute force: 
    - at each new window we recompute max (O(n^2))

observation:
    - each slide we remove a num and add a new one
        - could add new max or remove old one (or both)
        - adding new max is easy, 
            - compare to curr/prev max
        - removing non max is easy
        - how do we handle removing / replacing curr max?
            - keep track of next best/nextMax?
                - what if we boot second best? 
        =

ideas:
    - can we  keep counts of what is in the 
        - how do we determine max each time?
        - 
    - prefix and suffix max?
        - ideally it would be range query 
        - we can fake it using pref and suff sums
        - i.e look at max to right of left most bound max to left of right bound
            - breaks at k = 3, [1,1,1,2]
        - take smallest of the edge maxs if they arent the max?
            - breaks on [1,5,1,{0,4,2},6] k = 3, min fof 5,6 is 5 but max is 4
    - keep track of next best/nextMax
        - keep count of them?
        - consider [1  2  1  0  0 4  -2  6] 

    - use heap (max is at top of heap with idx 0)
        - once max falls out window we remove it from heap (keep removing)
            until max is inside window

    
"""
from heapq import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        slides = len(nums) - k
       
        heap = []

        for i, v in enumerate(nums[:k]):
            heap.append((-v,i))
        
        heapify(heap)
        res.append(-heap[0][0])
        for i in range(slides):
            start, end = i, i + k
            # print(f"heap: {heap}")
            # print(f"Window: {nums[start:end]}")
            v = nums[end]
            heappush(heap, (-v, end))
            
            while heap and heap[0][1] <= start:
                # print("p[p]")
                heappop(heap)
            # if start <= heap[0][1] <= end:
            #     res.append(-heap[0][0])
            # else:
            
            res.append(-heap[0][0])
            # print(f"res:{res}")

        return res