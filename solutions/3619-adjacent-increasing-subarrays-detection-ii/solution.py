class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        result = pre_len = l = 0
        for r in range(1, len(nums)):
            if nums[r]<=nums[r-1]:
                pre_len = r - l
                l = r

            result = max(result, min(pre_len, r - l + 1), (r - l + 1)//2)
        return result
