class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:    
        return sum([i for i in list(range(1,n+1)) if i%m!=0]) - sum(map(lambda x: x*m, range(1,n//m+1)))
        
