from collections import defaultdict

class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = defaultdict(int)
        

    def setCell(self, cell: str, value: int) -> None:       
        self.sheet[cell] = value
        return None
        

    def resetCell(self, cell: str) -> None:
        self.sheet[cell] = 0
        return None

    def getValue(self, formula: str) -> int:
        formula = formula[1:].split('+')
        try:
            x = int(formula[0])
        except:
            x =  self.sheet[formula[0]]
        
        try:
            y = int(formula[1])
        except:
            y =  self.sheet[formula[1]]
        
        return x + y
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
