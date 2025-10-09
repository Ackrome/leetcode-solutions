class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max2 = 0

        for i in range(n-1):
            if prices[i] < prices[i+1]:
                max2 += prices[i+1] - prices[i]
        return max2
