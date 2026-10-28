class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

                    
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            for d_r, d_c in directions:
                n_r, n_c = d_r + r, d_c + c
                dfs(n_r, n_c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        return res