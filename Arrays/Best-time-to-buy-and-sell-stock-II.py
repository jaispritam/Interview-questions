# leet code
# 122. Best Time to Buy and Sell Stock II


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Problem:
        Given an array 'prices' where prices[i] represents the stock price on day i,
        you can buy and sell multiple times, but can hold at most one share at a time.
        The goal is to calculate the maximum profit possible.

        Approach:
        - The idea is simple: whenever there's an increase in price (prices[i] > prices[i-1]),
          we can profit by buying on the previous day and selling on the current day.
        - We just keep summing up all such positive differences.
        """

        # Initialize variable to store the total profit
        total_profit = 0

        # Loop through prices starting from the second day
        for i in range(1, len(prices)):
            # Calculate profit difference between consecutive days
            daily_profit = prices[i] - prices[i - 1]

            # If there's a profit (price increased), add it to total profit
            if daily_profit > 0:
                total_profit += daily_profit

        # Return the total profit accumulated
        return total_profit
