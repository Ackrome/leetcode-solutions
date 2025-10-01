class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        empty = 0
        while numBottles>=numExchange:
            empty = numBottles%numExchange
            numBottles = numBottles//numExchange
            res+=numBottles
            numBottles+=empty
        return res
