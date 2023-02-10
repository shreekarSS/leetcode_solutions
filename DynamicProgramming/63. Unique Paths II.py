class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1

        # fill first row
        for r in range(1, rows):
            obstacleGrid[r][0] = int(obstacleGrid[r][0] == 0 and obstacleGrid[r - 1][0] == 1)

        # fill first col

        for c in range(1, cols):
            obstacleGrid[0][c] = int(obstacleGrid[0][c] == 0 and obstacleGrid[0][c - 1] == 1)

        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    obstacleGrid[r][c] = obstacleGrid[r - 1][c] + obstacleGrid[r][c - 1]

        return obstacleGrid[rows - 1][cols - 1]