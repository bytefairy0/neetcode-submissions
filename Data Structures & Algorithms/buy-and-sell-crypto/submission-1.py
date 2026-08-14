class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        buying_day = 0
        max_profit = 0

        for i in range(1, n):
            if prices[i] < prices[buying_day]:
                buying_day = i
            else:
                max_profit = max(max_profit, prices[i] - prices[buying_day])

        return max_profit
