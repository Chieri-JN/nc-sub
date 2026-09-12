"""
impletme time based kv store

we want to be able to store multiple values per key with timestamps
when we call get with a ts we want to be able to get the greatest ts <= to that timespamp
return "" if none

we can use binary search and binary insertion to make these operaitons O(logn)

"""
from bisect import bisect_right, insort_right
from collections import defaultdict 
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        insort_right(self.store[key], (timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_right(self.store[key], timestamp, key=lambda r: r[0])
        if idx:
            return self.store[key][idx - 1][1]
        else:
            return ""
