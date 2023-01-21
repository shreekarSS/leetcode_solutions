class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]
        """

        slow  = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow+=1
                