class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(map(lambda x: int(x), list(s)))
        n = len(s)
        for i in range(n-2):
            s_new = []
            for j in range(len(s)-1):
                to = (s[j]+s[j+1])%10
                s_new.append(to)
            s = s_new
        return s[0]==s[1]
