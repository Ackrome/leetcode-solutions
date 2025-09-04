class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x = abs(x-z)
        y = abs(y-z)

        if x<y:
            return 1
        elif y<x:
            return 2
        else:
            return 0
