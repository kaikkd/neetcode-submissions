class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heaps = []
        res = []
        for x, y in points:
            dis = x * x + y * y
            heaps.append([dis, x, y])
        
        heapq.heapify(heaps)
        while k > 0:
            k -= 1
            _, x, y = heapq.heappop(heaps)
            res.append([x, y])
        
        return res