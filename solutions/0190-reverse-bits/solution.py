class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = str(bin(n))[2:]
        bin_n = '0'*(32 - len(bin_n)) + bin_n
        return (int(bin_n[::-1],2))
