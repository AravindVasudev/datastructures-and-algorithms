# https://leetcode.com/problems/paint-house/
# https://www.lintcode.com/problem/515/

# Bottom Up
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        memo = [[-1] * 3 for _ in range(len(costs))]
        return self.computeMinCost(costs, 0, -1, memo)

    def computeMinCost(self, costs, index, prevPick, memo):
        if len(costs) == index:
            return 0

        if prevPick != -1 and memo[index][prevPick] != -1:
            return memo[index][prevPick]

        minimum = float('inf')
        for color, cost in enumerate(costs[index]):
            if color == prevPick:
                continue
            
            minimum = min(minimum,
                cost + self.computeMinCost(costs, index + 1, color, memo))

        memo[index][prevPick] = minimum
        return memo[index][prevPick]
