class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        pre_e = intervals[0][1]

        for s, e in intervals[1:]:
            if s >= pre_e:
                pre_e = e
            else:
                pre_e = min(pre_e, e)
                res += 1
        return res