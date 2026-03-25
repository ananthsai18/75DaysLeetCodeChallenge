class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxProfit=0
        minPrice=float("inf")
        for price in prices:
            if price < minPrice:
                minPrice=price
            else:
                profit=(price-minPrice)
                maxProfit=max(maxProfit,profit)
        return maxProfit


        