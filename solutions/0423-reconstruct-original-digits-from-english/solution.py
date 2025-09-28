from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        res = []
        per = {
            "0":"z",
            "2":"w",
            "4":"u",
            "6":"x",
            "8":"g",
            "1":"o",
            "3":"t",
            "5":"f",
            "7":"s",
            "9":"i"
        }
        tod = {
            "0":"zero",
            "2":"two",
            "4":"four",
            "6":"six",
            "8":"eight",
            "1":"one",
            "3":"three",
            "5":"five",
            "7":"seven",
            "9":"nine"
        }

        for key, value in per.items():

            counte = s.count(value)
            if counte:
                for letter in tod[key]:
                    s = s.replace(letter,'',counte)
                res.extend([key]*counte)
        
        return ''.join(sorted(res, key = lambda x:int(x)))

        
