class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = Counter(tasks)
        heap = tasks.values()
        heap = [-1 * n for n in heap]
        heapq.heapify(heap)

        time = 0
        q = deque()
        while heap or q:
            time += 1
            
            if not heap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt != 0:
                    q.append([cnt, time + n])
            
            if q and time == q[0][1]:
                heapq.heappush(heap, q.popleft()[0])
        
        return time