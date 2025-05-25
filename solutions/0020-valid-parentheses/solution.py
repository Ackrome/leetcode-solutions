class Solution:
    def isValid(self, s: str) -> bool:
        pars = [['(', ')'], ['{', '}'], ['[' ,']']]
        inn = {
            '(':0,
            '{':1,
            '[':2
        }
        out = {
            ')':0,
            '}':1,
            ']':2
        }
        line = []
        for i in s:
            if i in ['(','{','[']:
                line.append(inn[i])
            else:
                if len(line):
                    if line[-1]!=out[i]:
                        return False
                    else:
                        line.pop(-1)
                else:
                    return False
                
        if len(line):
            return False
        else:
            return True
