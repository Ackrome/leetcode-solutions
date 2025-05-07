class Solution:
    def convert(self, s: str, numRows: int) -> str:
        len_s = len(s)

        if len_s <= numRows or numRows == 1:
            return s
        else:
            array = []
            k=0

            symbols_between = numRows - 1
            
                
            while len_s>0:
                if k%symbols_between == 0:
                    array.append(list(s[:numRows]))
                    len_s -= numRows
                    s = s[numRows:]
                else:
                    saray = ['']*numRows
                    saray[-k%symbols_between] = s[0]
                    array.append(saray)
                    len_s -= 1
                    s = s[1:]
                k+=1

            
            
            res = ['']*numRows
            for i in range(numRows):
                res[i] = ''.join(array[j][i] for j in range(len(array)) if len(array[j])>=i+1)
                
            return (''.join(res))
