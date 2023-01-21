from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        _sum = 0

        hashMap = {0:0}


        for i  in range(len(nums)):
            _sum+= nums[i]

            if _sum%k not in hashMap:
                hashMap[_sum%k] = i+1

            elif hashMap[_sum%k] < i:
                return True

        return False

