"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        room = 0
        room_t = []
        for interval in intervals:
            s, e = interval.start, interval.end
            room_t.append((s, 1))
            room_t.append((e, -1))

        room_t.sort()

        cnt = 0
        for t in room_t:
            cnt += t[1]
            room = max(cnt, room)

        return room