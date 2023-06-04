class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        min_len = float("inf")
        for r in range(len(nums)):
            total+= nums[r]
            while total >= target:
                min_len = min( r-l+1,min_len)
                total-=nums[l]
                l+=1
            
        return 0 if min_len == float('inf') else min_len