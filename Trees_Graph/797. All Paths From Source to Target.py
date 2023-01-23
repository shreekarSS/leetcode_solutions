from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph)-1

        res = []


        def dfs(curr_node, path):

            if curr_node == target:
                res.append(list(path))
                return


            for next_node in graph[curr_node]:
                path.append(next_node)
                dfs(next_node, path)
                path.pop()

        dfs(0, [0])

        return res