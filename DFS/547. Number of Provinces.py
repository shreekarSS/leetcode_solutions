from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        noofProvince = 0
        visited = set()

        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if end not in visited and isConnected[start][end]:
                    dfs(end)

        for start in range(len(isConnected)):
            if start not in visited:
                visited.add(start)
                dfs(start)
                noofProvince+=1
