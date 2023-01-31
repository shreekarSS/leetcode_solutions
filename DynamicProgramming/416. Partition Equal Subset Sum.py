from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #solve using dynamic programming with bottom up tabulation
        #time complexity o(target*n), space complexity o(target)
        if not nums:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        dp = [True] + [False]*target
        #dp[0] is True always


        for num in nums:
            for i in range(target, num-1,-1):
                if dp[i-num]:# if i - num was previously achievable
                    dp[i] = True # dp[i] is also achievable32

        return dp[target]