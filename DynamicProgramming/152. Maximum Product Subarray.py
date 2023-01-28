from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_product = nums[0]
        max_product = nums[0]
        overall_product = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product

            min_product  = min(nums[i], min_product*nums[i])
            max_product = max( nums[i], max_product*nums[i])
            overall_product = max(overall_product, max_product)

        return overall_product