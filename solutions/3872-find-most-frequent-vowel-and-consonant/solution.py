from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        count = Counter(s)
        res = 0
        consonants = [count.get(i) for i in 'B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z'.lower().split(', ') if count.get(i)!=None]
        vowels = [count.get(i) for i in 'aeiou' if count.get(i)!=None]
        if consonants:
            res+=max(consonants)
        if vowels:
            res+=max(vowels)
        return res
