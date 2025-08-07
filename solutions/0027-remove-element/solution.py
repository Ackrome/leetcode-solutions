class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        count = nums.count(val)
        while val in nums:
            nums.remove(val)
        
        k = len(nums)
        nums.extend([count]*count)
        return k
        
