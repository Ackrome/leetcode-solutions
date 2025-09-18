
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = []
        
        for i in range(26):
            counts.append(s.count(chr(97 + i)))

        if 1 not in counts:
            return -1
        
        minidx = float('inf')
        
        for i in range(26):
            if counts[i] == 1:
                minidx = min(s.index(chr(97+i)), minidx)

        return minidx
        
