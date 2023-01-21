from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, dungeon_map: List[List[int]]) -> None:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        INF = 2147483647

        rows = len(dungeon_map)
        cols = len(dungeon_map[0])
        visited = set()

        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if dungeon_map[row][col] == 0:
                    queue.append((row,col))
                    visited.add((row,col))

        while queue:
            r,c = queue.popleft()
            for dr,dc in directions:
                nr= dr+r
                nc= dc+c
                if nr in range(rows) and nc in range(cols) and dungeon_map[nr][nc] == INF and ((nr,nc)) not in visited:
                    dungeon_map[nr][nc] = dungeon_map[r][c]+1
                    visited.add((nr,nc))


        print(dungeon_map)
