class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = Counter(tasks)
        heap = [-n for n in tasks.values()]
        heapq.heapify(heap)

        q = deque()
        time = 0
        while heap or q:
            time += 1
            if not heap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt != 0:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time