from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return dict([(value, key) for key,value in Counter(nums).items()])[1]

        
