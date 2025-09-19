class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = str(bin(x))[2:]
        y = str(bin(y))[2:]
        res = 0
        length = len(max([x,y],key = len))
        x = '0'*(length-len(x))+x
        y = '0'*(length-len(y))+y

        for i in range(length):
            if x[i]!=y[i]:
                res+=1
        return res
