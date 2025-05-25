
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        length = 0
        used = set()
        has_mid = False
        counte = Counter(words)
        nd = dict()
        for k,v in counte.items():
            if k not in used and counte.get(k[::-1],0)!=0:
                used.update([k,k[::-1]])
                
                if k!=k[::-1]:
                    nd[k+k[::-1]] = min(counte[k],counte[k[::-1]])*4
                else:
                    if counte[k]%2!=0:
                        if not has_mid:
                            nd['mid'] = 2
                            has_mid = True
                        nd[k] = (counte[k]-1)*2
                    else:
                        nd[k] = counte[k]*2
                
                    
                    
        return sum(nd.values())    
