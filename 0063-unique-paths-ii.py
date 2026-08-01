class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    obstacleGrid[r][c] = 1
                elif not obstacleGrid[r][c]:
                    up = 0 if r == 0 else obstacleGrid[r-1][c]
                    left = 0 if c == 0 else obstacleGrid[r][c-1]
                    obstacleGrid[r][c] = up + left
                else:
                    obstacleGrid[r][c] = 0
        return obstacleGrid[-1][-1]

