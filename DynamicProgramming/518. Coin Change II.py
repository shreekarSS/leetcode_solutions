from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0]*(amount+1)

        for coin in coins:
            #This loop iterates through each coin in the list coins.
            #The purpose of this loop is to use each coin to calculate the number of combinations for each amount.
            for amt in range(coin, amount+1):
                #the purpose of this loop is to calculate the number of combinations for each amount using the current coin.
                dp[amt]+= dp[amt-coin]

        return dp[amount]