class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        steps = [[] for i in range(n)]
        for i in range(1,n):
            for j in range(i):
                if i - j <= nums[j]:
                    steps[i].append(j)
        for i in range(1, n):
            mins = float('inf')
            for j in steps[i]:
                mins = min(mins, dp[j])
            dp[i] = mins+1
        return dp[n-1]
