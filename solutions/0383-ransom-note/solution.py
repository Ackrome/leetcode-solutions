from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        res = dict()
        for x in ransomNote:
            if x in magazine:
                res[x] = min(ransomNote[x], magazine[x])

        return res == dict(ransomNote)
