class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        q = deque()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            l_q = len(q)
            for i in range(l_q):
                r, c = q.popleft()
                for d_r, d_c in directions:
                    if (d_r + r in range(len(grid)) and d_c + c in range(len(grid[0])) 
                    and grid[d_r + r][d_c + c] == 1):
                        fresh -= 1
                        q.append((d_r + r, d_c + c))
                        grid[d_r + r][d_c + c] = 2
            time += 1
        
        return time if fresh == 0 else -1