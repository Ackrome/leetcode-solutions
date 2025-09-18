class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        n = len(s)
        if n==0:
            return True
        for i in t:
            if s[idx] == i:
                idx+=1
            if idx == n:
                return True
        return False
            
