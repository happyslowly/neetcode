# @leet start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_right, max_profit = 0, 0
        for i in range(len(prices) - 1, -1, -1):
            max_profit = max(max_profit, max_right - prices[i])
            max_right = max(max_right, prices[i])
        return max_profit


# @leet end

