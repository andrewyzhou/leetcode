class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows = [sum(grid[i]) for i in range(len(grid))]
        total = sum(rows)
        part = 0
        for i in range(len(rows)):
            part += rows[i]
            if part == total - part:
                return True
        cols = [sum([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[i]))]
        part = 0
        for i in range(len(cols)):
            part += cols[i]
            if part == total - part:
                return True
        return False