from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstN = float('inf')
        secondN = float('inf')


        for num in nums:
            if num <= firstN:
                firstN = num
            elif num <= secondN:
                secondN = num
            else:
                return True
        return False
    