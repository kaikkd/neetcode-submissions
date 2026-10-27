"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x : (x.start, x.end))
        pre_e = intervals[0].end

        for interval in intervals[1:]:
            s, e = interval.start, interval.end
            if s < pre_e:
                return False
            pre_e = e
        return True
