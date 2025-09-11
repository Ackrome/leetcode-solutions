class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        
        while n>0:
            if not any([n%2==0, n%3==0, n%5==0]):
                if n == 1:
                    return True
                else:
                    return False
            else:
                if n%2==0:
                    n//=2
                if n%3==0:
                    n//=3
                if n%5==0:
                    n//=5
        
