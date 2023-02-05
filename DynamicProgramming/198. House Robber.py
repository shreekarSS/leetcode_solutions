from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # o(n), o(n)

        dp = [0]*(len(nums)+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1,len(nums)):
            dp[i+1] = max(dp[i], dp[i-1]+nums[i])
        return dp[len(nums)]

    def rob1(self, nums: List[int]) -> int:
        # o(n), o(1)
        """
        [1,2,3,1]
        if  i want to rob 3, i have to check if 1+3 is greater or 2. 1+3 is greater, update rob1 and rob2

        """
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2