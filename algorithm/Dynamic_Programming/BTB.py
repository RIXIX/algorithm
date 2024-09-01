class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ma = 0
        ni = 999999
        for p in prices:

            if p < ni:
                ni = p
            else:
                ma = max(ma, p-ni)
        
        return ma


# 다른사람 풀이
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minP = prices[0]
        maxP = 0

        for price in prices:
            maxP = max(maxP, price - minP)
            minP = min(minP, price)

        return maxP