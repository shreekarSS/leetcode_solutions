from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_price = 0

        for i in range(len(prices)):
            min_price = min(min_price,prices[i])
            max_price = max(max_price, prices[i]-min_price)

        return max_price
