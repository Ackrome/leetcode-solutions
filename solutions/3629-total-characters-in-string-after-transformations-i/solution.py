class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        counts = [0] * 26
        
        for c in s:
            counts[ord(c) - ord('a')] += 1
        
        for _ in range(t):
            new_counts = [0] * 26
            z_count = counts[25]  # Count of 'z'
            
            new_counts[0] = z_count  # 'z' becomes 'a'
            new_counts[1] = (counts[0] + z_count) % MOD  # 'a' becomes 'b' and 'z' becomes 'b'
            
            for i in range(2, 26):
                new_counts[i] = counts[i - 1]  # Shift other characters
            
            for i in range(26):
                new_counts[i] %= MOD
            
            counts = new_counts
        
        return sum(counts) % MOD
