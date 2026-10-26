class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            res = heapq.heappop(heap) - heapq.heappop(heap)
            if res != 0:
                heapq.heappush(heap, res)
        
        return -heap[0] if heap else 0
