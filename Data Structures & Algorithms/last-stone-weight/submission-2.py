class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * n for n in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            res = abs(heapq.heappop(heap) - heapq.heappop(heap))
            if res:
                heapq.heappush(heap, -1 * res)
        
        return 0 if not heap else -heap[0]