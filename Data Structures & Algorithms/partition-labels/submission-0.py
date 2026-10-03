class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        res = []

        for i, v in enumerate(s):
            last_index[v] = i
        
        size, end = 0, 0
        for i, v in enumerate(s):
            end = max(end, last_index[v])
            size += 1

            if i == end:
                res.append(size)
                size = 0
        
        return res