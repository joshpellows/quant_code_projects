class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        buy_index = 0
        profit = 0
        i=1
        while i < len(prices):
            if profit < prices[i] - prices[buy_index] :
                profit = prices[i] - prices[buy_index]
                i+=1
            elif prices[i] < prices[buy_index]:
                buy_index = i
                i+=1
            else:
                i+=1
        return profit


