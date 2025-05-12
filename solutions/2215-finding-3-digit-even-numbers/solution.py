class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        uns = set()
        evens = set([i for i in digits if i%2==0])
    
        n = len(digits)
        
        for i in evens:
            digits.remove(i)
            to_add = []
            
            
            for j in range(n-1):
                if digits[j] == 0:
                    continue
                for k in range(n-1):
                    if k!=j:
                        uns.add(digits[j]*100+digits[k]*10+i)

            
            digits.append(i)
        
        return sorted(uns) 
