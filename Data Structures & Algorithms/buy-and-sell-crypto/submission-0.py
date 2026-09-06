"""
you pick a buy day 
you want to find a sell day, keep looking for a new as long as its >= current buy day
otherwise pick as new buy day and continue from there
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestSale = 0
        bPrice = prices[0]
        for i in range(1, len(prices)):
            currP = prices[i]
            if bPrice > currP:
                bPrice = currP
                continue
            else:
                bestSale = max(bestSale, currP - bPrice)

        return bestSale
