class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        stack = [] 
        
        for i in range(n):
            while stack and nums[i] > stack[-1][1]:  
                index, _ = stack.pop()
                ans[index] = i - index
            stack.append((i, nums[i]))
        
        return ans
