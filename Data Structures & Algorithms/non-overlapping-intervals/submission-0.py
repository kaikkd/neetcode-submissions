class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        pre_end = intervals[0][1]

        for s, e in intervals[1:]:
            if s >= pre_end:
                pre_end = e
            else:
                res += 1
                pre_end = min(pre_end, e)
        
        return res