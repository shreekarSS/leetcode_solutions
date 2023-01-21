from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """

        Input: nums = [4,5,6,7,0,1,2]
        Output: 0
        Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

        """
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left+right)//2

            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid

        return nums[left]



