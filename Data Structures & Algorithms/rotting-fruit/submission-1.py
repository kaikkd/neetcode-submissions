class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            lenght = len(q)
            for i in range(lenght):
                r, c = q.popleft()
                for d_r, d_c in directions:
                    i_r, i_c = d_r + r, d_c + c
                    if (0 <= i_r < len(grid) and 0 <= i_c < len(grid[0])
                    and grid[i_r][i_c] == 1):
                        fresh -= 1
                        grid[i_r][i_c] = 2
                        q.append((i_r, i_c))
            time += 1
        
        return time if fresh == 0 else -1