from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            left, right = 0, len(nums)-1

            while left < right:
                threeSum = a + nums[left] + nums[right]

                if threeSum < 0:
                    left+=1
                elif threeSum > 0:
                    right-=1
                else:
                    res.append([a, nums[left], nums[right]])

                    # since there is no return value here and we are looking for multiple triplets,
                    # increment left by 1 to check if it's prev value is same as its,
                    # then increment again
                    # Input: nums = [-1, 0, 1, 2, -1, -4]
                    #  Output: [[-1, -1, 2], [-1, 0, 1]]

                    left+=1

                    while nums[left] == nums[left-1] and left < right:
                        left+=1

            return res
