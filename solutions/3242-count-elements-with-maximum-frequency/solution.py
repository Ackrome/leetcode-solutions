from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        return sum([list(c.values())[i] for i in range(len(list(c.values())))  if list(c.values())[i] == max(list(c.values()))])
