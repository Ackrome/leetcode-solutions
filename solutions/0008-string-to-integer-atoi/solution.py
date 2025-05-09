class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        len_s = len(s)
        
        if not(len_s):
            return 0
        
        if s[0] == '-':
            sign = -1
            s = s [1:]
            len_s += -1
        elif s[0] == '+':
            sign = 1
            s = s [1:]
            len_s += -1
        else:
            sign = 1
            
        
        uns = ''            
        for i in range(len_s):
            cur = s[i]
            try:
                int(cur)
                uns+=cur
                if sign*int(uns) > 2**31 - 1:
                    return 2**31 - 1
                elif sign*int(uns) < -2**31:
                    return -2**31
            except:
                break
    
        try:
            return sign*int(uns)
        except:
            return 0
