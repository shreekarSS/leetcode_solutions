from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        count = 0

        row, col = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            area_count = 1

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if nr in range(row) and nc in range(col) and grid[nr][nc] == 1 and ((nr, nc)) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        area_count += 1
            return area_count

        li = []
        for r in range(row):
            for c in range(col):
                if ((r, c)) not in visited and grid[r][c] == 1:
                    visited.add((r, c))
                    ac = bfs(r, c)
                    li.append(ac)
        if li:
            return max(li)

        return 0