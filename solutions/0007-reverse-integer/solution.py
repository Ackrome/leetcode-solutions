class Solution:
    def reverse(self, x: int) -> int:
        strix = str(x)
        
        if strix[0] == '-':
            prefix = '-'
            strix = strix [1:]
        else:
            prefix = ''
        
        unstrix = strix[::-1]
        while unstrix.startswith('0'):
            unstrix = unstrix[1:]
        
        rev = prefix+unstrix
        if len(rev):
            uns = int(prefix+unstrix)
            return uns if uns > - 2 **31 and uns < (2**31 - 1) else 0
        else:
            return 0
