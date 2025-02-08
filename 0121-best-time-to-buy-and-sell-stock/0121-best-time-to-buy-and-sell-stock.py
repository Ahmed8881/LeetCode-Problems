class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        # First loop: Find the minimum price up to each day
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            # Calculate the profit by selling at the current price
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit  # Update max profit

        return max_profit
