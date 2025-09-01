import string

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        Title = []
        for i,let in enumerate(columnTitle):
            Title.append((string.ascii_uppercase.index(let)+1)*26**(n-i-1))
        return sum(Title)
