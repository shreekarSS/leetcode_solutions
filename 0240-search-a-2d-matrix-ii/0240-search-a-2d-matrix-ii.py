class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m, n = len(matrix), len(matrix[0])

        # left, right = 0, m*n-1

        # while left < right:
        #     mid = (left+right)//2
        #     ele = matrix[mid//n][mid%n]
        #     if target == ele:
        #         return True
        #     if target <ele:
        #         right = mid
        #     elif target > ele:
        #         left = mid+1
        # return False
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1

        return False
            