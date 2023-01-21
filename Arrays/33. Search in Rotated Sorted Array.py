from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4
        """


        left, right = 0, len(nums)-1


        while left <= right:
            mid = ( left+right) // 2

            if nums[mid]== target:
                return mid

            # check if left half is sorted

            if nums[left] <= nums[mid]:
                # check if target in range of left and mid
                if target in range(nums[left], nums[mid]):
                    right = mid-1
                else:
                    left = mid+1
            else:
                # check if right is sorted and target in btw mid+1 and right+1
                if target in range(nums[mid]+1, nums[right]+1):
                    left = mid+1
                else:
                    right = mid-1
        return -1