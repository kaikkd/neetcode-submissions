class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]

        for start, end in intervals:
            if start > output[-1][1]:
                output.append([start, end])
            else:
                output[-1][1] = max(end, output[-1][1])
        
        return output