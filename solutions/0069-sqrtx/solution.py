class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        if x == 0:
            return 0
        for i in range(40):
            r = (r + x / r) / 2
        return int(r)
