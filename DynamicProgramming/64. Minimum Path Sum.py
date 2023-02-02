from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid) , len(grid[0])

        #create dp array with extra layer, fill up with 'inf' values

        dp = [[float('inf')]*(col+1) for _ in range(row+1)]

        #set last element's right element or last element's bottom element to 0, for math workout, else code will fail

        dp[row-1][col] = 0

        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                # min btw either go down from the element or go right
                dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])

        return dp[0][0]