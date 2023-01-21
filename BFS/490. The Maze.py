from typing import List
from collections  import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        row, col = len(maze), len(maze[0])
        queue = deque()
        visited = set()
        def bfs(r,c):
            queue.append((r,c))
            visited.add((r,c))
            while queue:
                r,c = queue.popleft()
                if r == destination[0] and c == destination[1]:
                    return True

                for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                    newR, newC = r,c
                    while newR+dr in range(row) and newC+c in range(col) and maze[newR+dr][newC+dc] == 0:
                        newR+=dr
                        newC+=dc

                    if ((newR,newC)) not in visited:
                        queue.append((newR,newC))
                        visited.add((newR,newC))

        if bfs(*start):
            return True
        return False
    