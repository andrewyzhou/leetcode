class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                if c > 0 and r > 0:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
                elif c > 0:
                    grid[r][c] += grid[r][c-1]
                elif r > 0:
                    grid[r][c] += grid[r-1][c]
        return grid[-1][-1]
