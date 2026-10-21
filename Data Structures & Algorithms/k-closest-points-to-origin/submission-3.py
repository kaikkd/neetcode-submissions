class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            dis = x ** 2 + y ** 2
            heap.append((dis, x, y))
        heapq.heapify(heap)
        while k > 0:
            k -= 1
            _, x, y = heapq.heappop(heap)
            res.append([x, y])
        
        return res
