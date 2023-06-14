class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        occur = {0:1}
        counter = 0
        curSum= 0
        
        for i in range(len(nums)):
            curSum+= nums[i]
            
            
            if curSum - k in occur:
                counter+= occur[ curSum - k]
                
            if curSum in occur:
                occur[curSum]+=1
            else:
                occur[curSum] = 1
        return counter