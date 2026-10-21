"""
from hashlib import new
similar task msut be seperated by n cycles 

keep time ticker and each task is marked for when its next avail (t+n), add it to heap, 
if 

create map of task and freq, then go through this and add one for each task to heap, 

then pop heap and eather do task of wait


print(f"heapheap : {ready}")
            nextFree, _, task = heappop(ready)
            if nextFree > ticks:
                print(f"idle at {ticks}")
                ticks = nextFree

            taskFreqs[task] = taskFreqs.get(task, 0) - 1
            
            print(f"task {task} at {ticks}")
            if taskFreqs[task] > 0:
                fr = taskFreqs[task]
                newTime = ticks + n + 1
                print(f"{task} new time at {newTime}")
                heappush(ready, (newTime, -fr, task))
"""
from heapq import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreqs = {}
        total = len(tasks)
  
        for t in tasks:
            taskFreqs[t] = taskFreqs.get(t, 0) + 1

        taskQ = [(taskFreqs[t], t) for t in taskFreqs]
        taskQ.sort(reverse=True)

        taskPQ = [(i, -taskQ[i][0], taskQ[i][1]) for i in range(len(taskQ))]

        cnt = 0
        ticker = 0

        S = []
        while cnt < total:
            time, fr, task = heappop(taskPQ)
            if time <= ticker: 
                # S.append(task)
                cnt += 1 

                taskFreqs[task] = taskFreqs.get(task, 0) - 1
                if taskFreqs[task] > 0:
                    heappush(taskPQ, (time+n+1, fr+1, task))
            else:
                # S.append("Idle")
                heappush(taskPQ, (time, fr, task))

            ticker += 1
        # print(S)
        return ticker
        