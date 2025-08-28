import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        to_exclude = string.punctuation + string.whitespace
        for i in to_exclude:
            if i in s:
                s = s.replace(i,'')
        s = s.lower()
        
        return s == s[::-1]
        
