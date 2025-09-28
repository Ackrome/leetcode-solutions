class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = 0
        for i in range(2,len(nums)):
            if nums[i]<nums[i-1]+nums[i-2]:
                res = max(res, nums[i]+nums[i-1]+nums[i-2])
        return res
