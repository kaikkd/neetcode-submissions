class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh:
            l_q = len(q)
            for i in range(l_q):
                r, c = q.popleft()
                for d_r, d_c in directions:
                    n_r, n_c = r + d_r, c + d_c
                    if 0 <= n_r < ROWS and 0 <= n_c < COLS and grid[n_r][n_c] == 1:
                        grid[n_r][n_c] = 2
                        q.append((n_r, n_c))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
                 
