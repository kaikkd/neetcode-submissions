class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()

        for tp in triplets:
            if tp[0] > target[0] or tp[1] > target[1] or tp[2] > target[2]:
                continue
            
            for i, t in enumerate(tp):
                if t == target[i]:
                    res.add(i)
        
        return len(res) == 3