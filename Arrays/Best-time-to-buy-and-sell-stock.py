# leet code
# 121. Best Time to Buy and Sell Stock
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price to the first day's price
        buy_price = prices[0]
        # Initialize the maximum profit to 0
        profit = 0

        # Iterate over the prices starting from day 2
        for p in prices[1:]:
            # If the current price is less than our recorded buy price, update it
            if p < buy_price:
                buy_price = p
            
            # Calculate profit if we sold at current price, and update max profit
            profit = max(profit, p - buy_price)
        
        return profit
