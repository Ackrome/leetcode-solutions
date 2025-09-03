class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_let = list(set(s))
        t_let = list(set(t))

        if len(s_let)!=len(t_let) or len(s)!=len(t):
            return False

        else:
            per = dict()
            for i in range(len(s)):
                if s[i] in per.keys():
                    if per[s[i]] != t[i]:
                        return False
                else:
                    per[s[i]] = t[i]
                        
        return True
