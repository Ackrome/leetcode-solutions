class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = sorted(nums)
        cur_max = max(nums)
        cur_min = min(nums)

        if cur_min!=0:
            return 0
        
        if nums == list(range(0,cur_max+1)):
            return cur_max+1
        
        return list(set(range(0,cur_max+1)).difference(set(nums)))[0]
