# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        BUY, SELL = 0, 1
        N = len(prices)

        @cache
        def transact(day, transaction):
            if day == N:
                return 0

            if transaction == BUY:
                return max(transact(day + 1, SELL) - (prices[day] + fee),
                           transact(day + 1, BUY))
            else:
                return max(transact(day + 1, BUY) + prices[day],
                           transact(day + 1, SELL))

        return transact(0, BUY)

