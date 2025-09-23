from collections import defaultdict

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        difs = defaultdict(int)
        for i in range(1, int(area**0.5)+1):
            if area%i == 0:
                if area//i - i == 0:
                    return  [area//i, i]
                difs[area//i - i] = [area//i, i]

        return difs[min(list(difs.keys()))]
