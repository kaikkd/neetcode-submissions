class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        pre_e = intervals[0][1]
        for s, e in intervals[1:]:
            if pre_e <= s:
                pre_e = e
            else:
                res += 1
                pre_e = min(pre_e, e)
        
        return res