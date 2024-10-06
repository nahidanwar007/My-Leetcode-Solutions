class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0

        # for i in range(len(prices)-1):
        #     for j in range(i, len(prices)):
        #         if prices[j] > prices[i]:
        #             profit = max(profit, prices[j]-prices[i])
        
        # return profit

        j = 0
        profit = 0

        for i in range(len(prices)):
            if prices[i] > prices[j]:
                profit = max(profit, prices[i] - prices[j])
            else:
                j = i
        return profit
        