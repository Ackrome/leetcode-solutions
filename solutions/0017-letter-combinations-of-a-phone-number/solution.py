from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        perevodict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        n = len(digits)
        
        if n:
            pers = list(map(perevodict.get,digits))
            return list(map(lambda x: ''.join(x), product(*pers)))
        else:
            return []
