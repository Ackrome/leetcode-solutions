class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(list(s), key = ord)
        t = sorted(list(t), key = ord)
        s.append(None)

        for i in range(len(s)):
            if s[i]!=t[i]:
                return t[i]
