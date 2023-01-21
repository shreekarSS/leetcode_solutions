from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        if m == 0:
            return False

        left, right = 0, m*n -1

        while left <= right:
            pivot_idx = (left+right)//2
            pivot_element = matrix[pivot_idx//n][pivot_idx%n]

            if target == pivot_element:
                return True

            if target < pivot_element:
                right = pivot_idx-1
            else:
                left = pivot_idx+1
        return False

