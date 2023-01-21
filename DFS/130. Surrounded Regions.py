from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # capture border Os , mark them "T"
        # capture remaining Os , mark them "X"
        # mark Ts to O again


        row, col = len(board), len(board[0])

        def dfs(r,c):
            if r in range(row) and c in range(col) and board[r][c] == 'O':
                board[r][c]= 'T'
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r,c-1)
                dfs(r,c+1)

        # capture border O's and convert them to "T"
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O' and (r in [0, row-1] or c in [0, col-1]):
                    dfs(r,c)


        # capture remaninig Os and mark them 'X"
        for r in range(row):
            for c in range(col):
                if board[r][c]== 'O':
                    board[r][c] = 'X'
       # mark T's in to  Os
        for r in range(row):
            for c in range(col):
                if board[r][c] == "T":
                    board[r][c] = "O"

