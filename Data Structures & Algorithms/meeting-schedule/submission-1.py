"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
use sweep line, if cnt exceeds 1 then return false

sort
then for every start, end, +1, -1, 
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: (x.start, x.end))

        prev = None

        for curr in intervals:
            if prev and (prev.end > curr.end or prev.end > curr.start):
                return False

            prev = curr

        return True