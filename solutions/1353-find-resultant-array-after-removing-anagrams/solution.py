from collections import Counter
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        c = 0
        for i in range(1,n):
            if Counter(words[i-1 - c]) == Counter(words[i - c]):
                words.pop(i - c)
                c+=1
        return words
