class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            heap.append((x ** 2 + y ** 2, x, y))
        
        heapq.heapify(heap)
        while k > 0:
            k -= 1
            cur = heapq.heappop(heap)
            res.append([cur[1], cur[2]])
        
        return res