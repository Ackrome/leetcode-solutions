class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        value = -k
        n = len(nums)
        nums.sort()
        distinct = 1

        for i in range(1, n):
            value +=1
            diff = nums[i] - nums[i-1]
            value = max(value - diff, -k)
            if value > k:
                value = k
            else:
                distinct+=1
        return distinct
