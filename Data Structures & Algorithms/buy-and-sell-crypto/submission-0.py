class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            profit = price - min_price
            max_profit = max(profit, max_profit)
            min_price = min(price, min_price)
        return max_profit