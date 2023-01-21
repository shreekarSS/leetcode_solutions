from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # use bfs multi source, take count of fresh oranges and rotten

        min_time, fresh_oranges = 0, 0

        row, col = len(grid), len(grid[0])

        queue = deque()
        visited = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh_oranges+=1
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while queue and fresh_oranges > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr = dr+r
                    nc = dc+c
                    if grid[nr][nc] == 1 and nr in range(row) and nc in range(col) and ((nr,nc)) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
                        fresh_oranges-=1

            min_time+=1


        return min_time if fresh_oranges == 0 else -1




