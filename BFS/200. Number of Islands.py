from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        num_rows, num_cols  = len(grid), len(grid[0])
        visitedSet = set()
        counter= 0
        def bfs(r,c):
            queue = deque()
            queue.add((r,c))
            visitedSet.add((r,c))

            while queue:
                r,c = queue.popleft()
                delta_row = [-1, 0, 1, 0]
                delta_col = [0, 1, 0, -1]
                for i in range(len(delta_row)):
                    neigh_row = r+ delta_row[i]
                    neigh_col = c + delta_col[i]
                    if neigh_row in range(num_rows) and neigh_col in range(num_cols) and grid[neigh_row][neigh_col] == "1" and ((neigh_row, neigh_col)) not in visitedSet:
                        queue.append((neigh_row, neigh_col))
                        visitedSet.add((neigh_row,neigh_col))
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1" and ((row,col)) not in visitedSet:
                    bfs(row,col)
                    counter+=1


        return counter
