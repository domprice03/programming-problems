from numpy import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_seen = inf
        max_profit = 0

        for price in prices:
            profit = price - lowest_seen
            
            if profit > max_profit:
                max_profit = profit
            
            if price < lowest_seen:
                lowest_seen = price

        return max_profit
 