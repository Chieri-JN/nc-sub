"""

"""
from collections import defaultdict
from heapq import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = defaultdict(int)
        total = 0
        for t in tasks:
            taskFreq[t] += 1
            total += 1
        
        counts = []
        for tf in taskFreq:
            tfc = taskFreq[tf]
            counts.append((tfc, tf))

        counts.sort(reverse=True)

        taskQ = []
        for i, (tfc, tf) in enumerate(counts):
            taskQ.append((i, -tfc, tf))

        heapify(taskQ)

        ticks = 0
        count = 0
        # timeline = []
        while count < total:
            time, freq, task = heappop(taskQ)
            if time <= ticks: 
                # timeline.append(task)
                newTime, newfreq = time + n + 1, freq + 1
                count += 1
                if newfreq < 0:
                    bundle = (newTime, newfreq, task)
                    heappush(taskQ, bundle)
            else:
                bundle = (time, freq, task)
                heappush(taskQ, bundle)
                # timeline.append("Idle")

            ticks += 1

        # print(timeline)
        return ticks





            
