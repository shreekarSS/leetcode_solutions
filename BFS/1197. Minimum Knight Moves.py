from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        visited = set()
        def bfs(r,c):
            queue = deque()
            queue.append((0,0))
            visited.add((0,0))
            steps = 0

            while queue:
                for _ in range(len(queue)):
                    r,c = queue.popleft()
                    if r == x and c == y:
                        return steps

                    for dr,dc in (offsets):
                        nr = dr+r
                        nc = dc+c
                        if ((nr,nc)) not in visited:
                            queue.append((nr,nc))
                            visited.add((nr,nc))
                steps+=1

        return bfs(x,y)



obj = Solution()
print(obj.minKnightMoves(5,5))