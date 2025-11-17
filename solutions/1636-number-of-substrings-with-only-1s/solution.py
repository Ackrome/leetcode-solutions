class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        count = 0
        
        for ch in s:
            if ch == '0':
                ans += count * (count + 1) // 2
                ans %= MOD
                count = 0
            else:
                count += 1
        
        ans += count * (count + 1) // 2
        ans %= MOD
        
        return ans
