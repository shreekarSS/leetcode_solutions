from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        target = (rows-1,cols-1)

        if grid[0][0] == target and k > grid[0][0]:
            return 0


        visited = set()

        queue = deque()
        steps = 0
        queue.append((0,0,steps,k))
        visited.add((0,0,k))

        while queue:
            r, c, steps, obstacles_left = queue.popleft()

            if (r,c) == target:
                return steps

            for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                nr = dr+r
                nc = dc+c
                if nr in range(rows) and nc in range(cols):
                    obstacles_left_updated = obstacles_left-grid[nr][nc]
                    if obstacles_left_updated >= 0 and ((nr,nc,obstacles_left_updated)) not in visited:
                        visited.add((nr,nc,obstacles_left_updated))
                        queue.append((nr,nc,steps+1, obstacles_left_updated))


        return -1