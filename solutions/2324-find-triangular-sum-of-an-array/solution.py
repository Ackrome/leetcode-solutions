from math import comb
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)-1
        return sum([comb(n,i)*nums[i] for i in range(n+1)])%10
