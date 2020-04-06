class Solution:
    # Can first sell than buy in one day
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        while i < (len(prices) - 1):
            while i < len(prices)-1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i < len(prices)-1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            maxprofit += peak-valley
        return maxprofit
    def maxProfit2(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                maxprofit+=prices[i]-prices[i-1]
        return maxprofit        