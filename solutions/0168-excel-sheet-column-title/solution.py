class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber>0:
            columnNumber-=1
            rem = columnNumber % 26
            result = chr(65+rem) + result
            columnNumber //=26
            
        return result
