from collections import Counter

class Solution:
    def deleteAndEarn(self, power: List[int]) -> int:
        f = Counter(power)
        values = sorted(f.keys())
        n = len(values)
        dp = [0]*n
        for i in range(n):
            d = values[i]
            total = d*f[d]
            j = i - 1
            while j >= 0 and values[j] >= d - 1:
                j -= 1
            
            if j>=0:
                total += dp[j]
            
            dp[i] = max(dp[i - 1] if i >0 else 0, total)
        
        return dp[-1]
