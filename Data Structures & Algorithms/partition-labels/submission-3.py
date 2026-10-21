class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        for i, v in enumerate(s):
            last_idx[v] = i
        
        res = []
        end, size = 0, 0
        for i, v in enumerate(s):
            size += 1
            end = max(end, last_idx[v])

            if end == i:
                res.append(size)
                size = 0
        
        return res