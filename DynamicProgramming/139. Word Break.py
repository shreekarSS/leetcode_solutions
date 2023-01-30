from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Input: s = "leetcode", wordDict = ["leet","code"]
        Output: true
        Explanation: Return true because "leetcode" can be segmented as "leet code".
        """
        dp = {}

        def dfs(start_index):

            if start_index == len(s):
                return True

            if start_index in dp:
                return dp[start_index]

            ans = False
            for word in wordDict:
                if s[start_index:].startswith(word):
                    if dfs(start_index+len(word)):
                        ans = True
                        break
            dp[start_index] = ans
            return ans
        return dfs(0)