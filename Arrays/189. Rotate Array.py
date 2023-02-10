from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # if k is greater than len(nums)
        k%= n
        # call reverse three times
        # reverse whole array
        # reverse 0 to k-1
        # reverse k to n-1

        self.reverse(nums, 0, n-1)
        self.reverse(nums,0, k-1)
        self.reverse(nums, k, n-1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start+1, end-1
 
