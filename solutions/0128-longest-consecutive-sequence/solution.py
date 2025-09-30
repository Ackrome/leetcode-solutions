class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        n = len(nums)
        first = 0
        second = 0
        res = 0
        for i in range(n):
            if nums[i]-nums[second]==1:
                second +=1
            else:
                res = max(second - first + 1, res)
                first = i
                second = i
        res = max(second - first + 1, res)

        return res
