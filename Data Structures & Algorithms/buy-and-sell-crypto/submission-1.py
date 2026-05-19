class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = prices[0]
        maxProfit = 0

        for price in prices :
            maxProfit = max(maxProfit,price - minPrice)

            if minPrice > price :
                minPrice = price
                

        return maxProfit