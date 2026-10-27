class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        stack = [intervals[0]]
        
        res = 0

        for start, end in intervals[1:]:
            if start >= stack[-1][1]:
                stack.append([start, end])
            else:
                stack[-1][1] = min(stack[-1][1], end)
                res += 1
        
        return res