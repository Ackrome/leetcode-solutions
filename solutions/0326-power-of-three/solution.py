class Solution:
    def isPowerOfThree(self, n: int) -> bool:     
        return n in [3**i for i in range(41)]
