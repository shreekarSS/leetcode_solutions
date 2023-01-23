from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:


        def dfs(index, path):

            if len(path) == k:
                output.append(path)


            for i in range(index, n+1):
                path.append(i)
                dfs(i+1,path)
                path.pop()

        output = []

        dfs(1, [])

        return output