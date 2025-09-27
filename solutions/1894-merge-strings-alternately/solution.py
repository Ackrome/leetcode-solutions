class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        s = max(n,m)
        res = ['_']*s*2
        print(res)
        res[::2] = list(word1)+['_']*(s-n)
        res[1::2] = list(word2)+['_']*(s-m)
        return ''.join(res).replace('_','')
