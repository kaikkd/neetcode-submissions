"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for interval in intervals:
            time.append((interval.start, 1))
            time.append((interval.end, -1))
        
        res = cnt = 0
        time.sort()
        for i in time:
            cnt += i[1]
            res = max(res, cnt)
        
        return res