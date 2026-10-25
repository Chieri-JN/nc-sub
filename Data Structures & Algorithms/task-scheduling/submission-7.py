"""

"""
from collections import defaultdict
from heapq import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = defaultdict(int)
        maxFreq = 0
        total = 0
        
        for t in tasks:
            taskFreq[t] += 1
            maxFreq = max(maxFreq, taskFreq[t])
            total += 1
        countAtMax = 0
        for t in taskFreq:
            if taskFreq[t] == maxFreq:
                countAtMax += 1

        
        spaced = (n+1) * (maxFreq-1) + countAtMax
        # total += 1

        return max(spaced, total)

        





            
