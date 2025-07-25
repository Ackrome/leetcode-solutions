class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))[::-1]
        result = 0
        was_summed = False
        for i in nums:
            if i >= 0:
                was_summed = True
                result+=i
        
        if not(was_summed):
            result+=nums[0]
            
        
        return result
        
