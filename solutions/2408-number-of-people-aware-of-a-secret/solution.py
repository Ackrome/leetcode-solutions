MODULO = 10**9+7

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [1]+[0]*(n-1)
        for i in range(1,n):
            dp[i] = (sum([dp[i-j] for j in range(delay,forget)]) + MODULO)%MODULO

        return sum(dp[n-forget:])%MODULO
