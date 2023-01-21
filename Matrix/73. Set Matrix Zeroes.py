from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # with time complexity O(m*n), space O(m+n)
        row , col = len(matrix), len(matrix[0])

        rows,cols = [False]*row, [False]*col


        for r in range(row):
            for c in range(col):
                if matrix[r][c]==0:
                    rows[r] = True
                    cols[c] = True

        for r in range(row):
            for c in range(col):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0

        # with time complexity O(m*n), space O(1)

        row = len(matrix)
        col = len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    if r == 0:
                        first_row_has_zero = True
                    if c == 0:
                        first_col_has_zero = True
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1,row):
            for c in range(1,col):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if first_row_has_zero:
            for c in range(col):
                matrix[0][c] = 0
        if first_col_has_zero:
            for r in range(row):
                matrix[r][0] = 0
