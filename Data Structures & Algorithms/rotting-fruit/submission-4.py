class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        q = deque()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while fresh and q:
            l_q = len(q)
            for i in range(l_q):
                r, c = q.popleft()
                for d_r, d_c in directions:
                    n_r, n_c = d_r + r, d_c + c
                    if 0 <= n_r < ROWS and 0 <= n_c < COLS and grid[n_r][n_c] == 1:
                        grid[n_r][n_c] = 2
                        fresh -= 1
                        q.append((n_r, n_c))
            time += 1
        
        return time if not fresh else -1