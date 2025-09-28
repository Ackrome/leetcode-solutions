from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dtext = dict(Counter(text))
        balloon = {
            "a":1,
            "b":1,
            "l":2,
            "o":2,
            "n":1
        }
        sb = set("balloon")
        db = False
        res=0
        while (sb & set(dtext.keys())) == sb:
            for key in balloon.keys():
                if dtext[key]>=balloon[key]:
                    dtext[key]-=balloon[key]
                else:
                    db = True
                    break
            if db:
                break
            res+=1
        return res
