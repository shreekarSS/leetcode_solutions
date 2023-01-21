from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(n)}

        for node, edge in edges:
            preMap[node].append(edge)
            preMap[edge].append(node)


        visitedSet = set()

        def dfs(node, parent):
            visitedSet.add(node)
            for neigh in preMap[node]:
                if neigh == parent:
                    continue
                if neigh in visitedSet:
                    return False

                if not dfs(neigh, node):
                    return False
            return True


        return dfs(0,-1) and len(visitedSet) == n