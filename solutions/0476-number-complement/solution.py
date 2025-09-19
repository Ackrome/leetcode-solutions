class Solution:
    def findComplement(self, num: int) -> int:
        return sum([int(str(bin(num))[2:].replace('1','2').replace('0','1').replace('2','0')[::-1][i])*2**i for i in range(len(str(bin(num)))-2)])
