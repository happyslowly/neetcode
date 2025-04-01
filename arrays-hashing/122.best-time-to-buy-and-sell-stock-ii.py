# @leet start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        last_price, profit = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] > last_price:
                profit += prices[i] - last_price
            last_price = prices[i]
        return profit


# @leet end

