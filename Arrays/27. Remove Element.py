from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # same logic as moving zeros to end

        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow+=1
        return slow
