# 121.Leet code
# Best Time to Buy and Sell Stock

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate the maximum profit from a single buy-sell transaction.

        Args:
        prices (List[int]): List of stock prices where prices[i] is the price on day i.

        Returns:
        int: Maximum profit achievable. Returns 0 if no profit is possible.
        """

        # Initialize the minimum price with the first day's price
        buy_price = prices[0]

        # Initialize maximum profit to 0
        profit = 0

        # Iterate over the prices starting from the second day
        for price in prices[1:]:
            # If the current price is lower than our recorded buy_price,
            # update buy_price to this lower price (we want to buy at the lowest price)
            if price < buy_price:
                buy_price = price
            
            # Calculate potential profit if we sell at the current price
            potential_profit = price - buy_price

            # Update profit if potential_profit is greater than current profit
            profit = max(profit, potential_profit)
        
        # Return the maximum profit found
        return profit

