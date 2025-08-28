class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex+1
        if numRows == 1:
            return [[1]][0]
        result = [[1]]*numRows
        for i in range(numRows-1):
            result[i+1] = [1]+[result[i][0+el]+result[i][1+el] for el in range(i)]+[1]
        return result[rowIndex]
