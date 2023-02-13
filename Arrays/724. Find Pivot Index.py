from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, v in enumerate(nums):
            if left_sum == (total_sum-left_sum-v):
                return i
            left_sum+=v
        return -1
