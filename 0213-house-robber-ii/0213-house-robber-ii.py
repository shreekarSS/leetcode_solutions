class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_helper(subNums):
            rob1, rob2 = 0, 0

            for num in subNums:
                temp = max(num+rob1 , rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        n = len(nums)
        firstSub = nums[1:]
        secondSub = nums[:-1]

        return max(nums[0], rob_helper(firstSub), rob_helper(secondSub))
