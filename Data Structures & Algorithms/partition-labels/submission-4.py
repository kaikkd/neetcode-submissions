class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_far = {}
        for i, c in enumerate(s):
            s_far[c] = i
        
        res = []
        farthest = 0
        length = 0
        for i, c in enumerate(s):
            farthest = max(farthest, s_far[c])
            length += 1
            if i == farthest:
                res.append(length)
                length = 0
        
        return res