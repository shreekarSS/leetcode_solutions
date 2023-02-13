from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])

        left, right = 0, n-1

        while left < right:
            mid_col = (left+right)//2
            mid_row = max(range(m), key=lambda x: mat[x][mid_col])
            if mat[mid_row][mid_col] > mat[mid_row][mid_col+1]:
                right = mid_col
            else:
                left = mid_col+1

        col  = left
        row = max(range(m), key=lambda x: mat[x][col])
        return [row, col
                ]