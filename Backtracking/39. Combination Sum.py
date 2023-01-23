from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Input: candidates = [2,3,6,7], target = 7
        Output: [[2,2,3],[7]]
        Explanation:
        2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
        7 is a candidate, and 7 = 7.
        These are the only two combinations.
        """

        res = []

        def dfs(start, comb, rem):

            if rem == 0:
                res.append(list(comb))
                return

            elif rem < 0:
                return


            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                dfs(start,comb,rem-candidates[i])
                comb.pop()

        dfs(0,[],target)