class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        for word in text.split():
            res+= 1 if not any([i in word for i in brokenLetters]) else 0
        return res
