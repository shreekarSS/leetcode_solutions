from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        preMap  = {i: [] for i in range(n)}
        visited = set()
        #fill the pre map
        for node, edge in edges:
            preMap[node].append(edge)
            preMap[edge].append(node)

        #call dfs on source

        def dfs(source):
            if source == destination:
                return True

            visited.add(source)
            for neigh in preMap[source]:
                if neigh not in visited and dfs(neigh):
                    return True

            return False

        return dfs(source)
