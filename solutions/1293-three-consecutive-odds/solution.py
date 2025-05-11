class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        is_odd = 0
        
        for i in arr:
            if i%2 == 1:
                is_odd +=1
            elif i%2 == 0:
                is_odd = 0
            
            if is_odd==3:
                return True
        
        return False
