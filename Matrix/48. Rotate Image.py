from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        left , right = 0, len(matrix[0])-1

        while left < right:
            for i in range(right-left):
                top, bottom  = left, right

                top_left = matrix[top][left+i]

                matrix[top][left+i] = matrix[bottom-i][left]

                matrix[bottom-i][left] = matrix[bottom][right-i]

                matrix[bottom][right-i] = matrix[top+i][right]

                matrix[top+i][right] = top_left

