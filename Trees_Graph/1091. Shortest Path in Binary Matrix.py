from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        visitedSet = set()
        distance = 1

        if grid[0][0] != 0 or grid[row-1][col-1] != 0:
            return -1

        queue = deque()
        queue.append((0,0))
        visitedSet.add((0,0))
        while queue:
            for _ in range(queue):
                r,c = queue.popleft()
                if (r,c) == (row-1,col-1):
                    return distance
                for dr,dc in directions:
                    nr = dr+r
                    nc = dc+c
                    if nr in range(row) and nc in range(nc) and grid[nr][nc] == 0 and ((nr,nc)) not in visitedSet:

                        visitedSet.add((nr,nc))
                        queue.append((nr,nc))

            distance+=1

        return -1
