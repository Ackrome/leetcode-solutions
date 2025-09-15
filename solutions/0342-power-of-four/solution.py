class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n in [4**i for i in range(20)]
