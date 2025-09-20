class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper().replace('-','')[::-1]
        res = ''
        for i in range(len(s)):
            res += s[i]
            if (i+1)%k==0 and i!=len(s)-1:
                res += '-'
        return res[::-1]



