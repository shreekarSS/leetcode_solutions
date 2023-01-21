from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap  = {i : [] for i in range(n)}

        visitedSet = set()
        component = 0
        for node , edge in edges:
            preMap[node].append(edge)
            preMap[edge].append(node)

        def dfs(node):
            for neigh in preMap[node]:
                if neigh not in visitedSet:
                    visitedSet.add(neigh)
                    dfs(neigh)



        for node in preMap:
            if node in visitedSet:
                continue

            visitedSet.add(node)
            dfs(node)
            component+=1

        return component


