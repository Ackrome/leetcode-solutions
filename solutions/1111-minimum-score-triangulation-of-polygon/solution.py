class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for L in range(2,n):
            for i in range(n-L):
                j=i+L
                dp[i][j] = float('inf')
                for k in range(i+1, j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    dp[i][j] = min(dp[i][j], cost)
        return dp[0][n-1]

