class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        s = min(list(map(abs, nums)))
        res = []
        for i in nums:
            if abs(i) == s:
                res.append(i)
        return max(res)
