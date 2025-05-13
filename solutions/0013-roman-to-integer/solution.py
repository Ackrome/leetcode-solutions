class Solution:
    def romanToInt(self, s: str) -> int:
        
        n = len(s)
        perevodict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        
        for i in range(n-1):
            cur = perevodict[s[i]] if perevodict[s[i]]>=perevodict[s[i+1]] else -perevodict[s[i]]
            res += cur
        
        
        return res + perevodict[s[-1]]
