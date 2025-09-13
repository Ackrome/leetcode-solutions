class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s, t = pattern, s.split()
        s_let = list(set(s))
        t_let = list(set(t))

        if len(s_let)!=len(t_let) or len(s)!=len(t):
            return False

        else:
            per = dict()
            for i in range(len(s)):
                if s[i] in per.keys():
                    
                    if per[s[i]] != t[i]:
                        print(per, s[i], t[i])
                        return False
                else:
                    per[s[i]] = t[i]
                        
        return True
