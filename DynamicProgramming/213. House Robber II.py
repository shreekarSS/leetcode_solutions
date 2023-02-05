from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Input: nums = [2,3,2]
        Output: 3
        Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
        """
        # so have util function from house robber 1, apply that to nums[1:] , then nums[:-1]
        # compare max btw nums without first element, and nums without last element
        def rob_helper(subnums):
            rob1, rob2 = 0, 0

            for num in subnums:
                temp = max(num+rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        max(nums[0], rob_helper(nums[1:], rob_helper(nums[:-1])))
