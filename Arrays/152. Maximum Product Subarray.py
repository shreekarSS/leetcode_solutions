from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = nums[0]
        max_prod = nums[0]
        overall_max= nums[0]

        for i in range(1, len(nums)):

            if nums[i] < 0:
                min_prod, max_prod = max_prod, min_prod

            min_prod = min(nums[i], min_prod*nums[i])
            max_prod = max(nums[i], max_prod*nums[i])
            overall_max = max(max_prod, overall_max)

        return overall_max