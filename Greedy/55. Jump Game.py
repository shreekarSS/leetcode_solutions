from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump_index = 0

        for i in range(len(nums)):
            if i > max_jump_index:
                return False
            # max_jump is index + nums[i], meaning,i can jump to max_jump in total
            # for ex: i=0, nums[i]= 2, max_jump =2, i can reach nums[2]
            # i=1 , nums[i]= 3, max_jump =4, i can jump to nums[4]
            # i=2, nums[i]= 1, max_jump= 3, i can jump to nums[3]

            max_jump_index = max(max_jump_index, nums[i]+i)
        return True
