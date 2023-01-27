from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = {}  # where each r,c 's LIP is stored

        def dfs(r, c, preVal):
            if not (r in range(row)) or not (c in range(col)) or matrix[r][c] <= preVal:
                return 0

            lip = 1

            if (r, c) in dp:
                return dp.get((r, c))

            lip = max(lip, 1 + dfs(r - 1, c, matrix[r][c]))
            lip = max(lip, 1 + dfs(r + 1, c, matrix[r][c]))
            lip = max(lip, 1 + dfs(r, c - 1, matrix[r][c]))
            lip = max(lip, 1 + dfs(r, c + 1, matrix[r][c]))

            dp[(r, c)] = lip
            return lip

        for r in range(row):
            for c in range(col):
                dfs(r, c, -1)

        return max(dp.values())
