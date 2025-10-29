class Solution:
    def smallestNumber(self, n: int) -> int:
        return (2**ceil(log2(n+1)) - 1)
