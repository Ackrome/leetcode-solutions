class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i]:
                continue
            if sum(nums[:i]) == sum(nums[i:]):
                count+=2
            elif abs(sum(nums[:i]) - sum(nums[i:])) == 1:
                count+=1

        return count
