from collections import defaultdict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        been = defaultdict(int)
        shift = 0
        for i in range(len(nums)):
            been[nums[i-shift]]+=1
            if been[nums[i-shift]]>2:
                del nums[i-shift]
                shift+=1
        return len(nums)
