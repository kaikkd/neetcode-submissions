"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort(key = lambda x : x.start)
        pre_e = intervals[0].end
        for interval in intervals[1:]:
            if pre_e > interval.start:
                return False
            else:
                pre_e = interval.end
        
        return True