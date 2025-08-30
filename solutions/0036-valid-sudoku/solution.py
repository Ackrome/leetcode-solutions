from collections import Counter
from functools import reduce

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(*board, sep='\n')
        for i in range(9):
            countr1 = Counter(board[i])
            countr1.pop('.')
            
            countr2 = Counter([board[j][i] for j in range(9)])
            countr2.pop('.')
            if any([el>=2 for el in list(countr1.values())+list(countr2.values())]):
                return False
        
        
        for i in range(3):
            for j in range(3):
                countr = Counter(list(reduce(lambda x,y: x+y , map(lambda x: x[j*3:j*3+3], board[i*3:i*3+3]))))
                countr.pop('.')
                if any([el>=2 for el in list(countr.values())]):
                    return False
        
        return True
