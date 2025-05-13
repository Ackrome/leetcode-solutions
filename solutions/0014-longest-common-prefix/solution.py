class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min(strs, key = len)
        cur = ''
        if len(strs) == 1:
            return strs[0]
        
        for i in n:
            
            if not all([j.startswith(cur + i) for j in strs]):
                
                return cur
            else:
                cur +=i
                
        return cur 
