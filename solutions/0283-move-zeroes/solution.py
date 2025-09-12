class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countz = 0
        for i in range(len(nums)):
            if nums[i-countz]==0:
                nums.pop(i-countz)
                nums.append(0)
                countz+=1
