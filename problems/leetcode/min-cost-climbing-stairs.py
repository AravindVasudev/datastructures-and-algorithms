# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        
        two_step_prev, one_step_prev = cost[0], cost[1]
        current_step = 0
        for i in range(2, len(cost)):
            current_step = min(one_step_prev, two_step_prev) + cost[i]
            two_step_prev = one_step_prev
            one_step_prev = current_step
            
        return min(one_step_prev, two_step_prev)
