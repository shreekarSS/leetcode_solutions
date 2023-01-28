from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row, col = len(heights), len(heights[0])

        pac, atl = set(), set()


        def dfs(r,c, visit, prevHeight):
            if ((r,c)) in visit or not(r in range(row)) or not(c in range(col)) or prevHeight > heights[r][c]:
                return
            visit.add((r,c))
            dfs(r-1,c,visit,heights[r][c])
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])

        for c in range(col):
            dfs(0,c,pac,heights[0][c])
            dfs(row-1,c,atl, heights[row-1][c])

        for r in range(row):
            dfs(r,0,pac,heights[r][0])
            dfs(r,col-1, atl, heights[r][col-1])

        output = []
        for r in range(row):
            for c in range(col):
                if ((r,c)) in pac and ((r,c )) in atl:
                    output.append([r,c])

        return  output

