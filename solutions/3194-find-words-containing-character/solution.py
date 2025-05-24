class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        uns = []
        n = len(words)
        
        for i in range(n):
            if x in words[i]:
                uns.append(i)
        return uns
