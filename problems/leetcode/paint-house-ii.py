# https://leetcode.com/problems/paint-house-ii/
# https://www.lintcode.com/problem/516/description
# Solution: https://www.cnblogs.com/airwindow/p/4804011.html

class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        if len(costs) == 0:
            return 0

        K = len(costs[0])
        dp = [0] * K
        min1, min2 = 0, 0

        for house in range(1, len(costs) + 1):
            prevMin1, prevMin2 = min1, min2
            min1, min2 = float('inf'), float('inf')

            for color in range(K):
                if prevMin1 == dp[color]:
                    dp[color] = prevMin2 + costs[house - 1][color]
                else:
                    dp[color] = prevMin1 + costs[house - 1][color]

                if dp[color] <= min1:
                    min1, min2 = dp[color], min1
                elif dp[color] < min2:
                    min2 = dp[color]
        
        return min(dp)