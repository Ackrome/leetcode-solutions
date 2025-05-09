class Solution:
    def convert(self, s: str, numRows: int) -> str:
        len_s = len(s)

        if len_s <= numRows or numRows == 1:
            return s
        
        
        cur_index = 0
        delta = 1
        rows = [[] for i in range(numRows)]
        
        for bukva in s:
            rows[cur_index].append(bukva)
            if cur_index == 0:
                delta = 1
            
            elif cur_index == numRows - 1:
                delta = -1 
            
            cur_index += delta
        
        return ''.join([''.join(rows[i]) for i in range(numRows)])
