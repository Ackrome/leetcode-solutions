class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums:
            return None
        nums = list(set(nums))
        if  3 > len(nums):
            return max(nums)
        return sorted(nums)[-3]
