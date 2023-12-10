# https://leetcode.com/problems/maximum-performance-of-a-team/
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7

        # Order the engineers from most to least efficiency.
        # This way, when we traverse in order, we'd be picking the 
        # next highest efficiency of engineers in order, hence
        # maximizing efficienct.
        engineers = sorted(list(zip(efficiency, speed)), key=lambda x: -x[0])

        performance, totalSpeed = 0, 0
        speedHeap = []

        for e, s in engineers:
            totalSpeed += s
            heapq.heappush(speedHeap, s)

            # If we have more than k engineers, pop the slowest engineer.
            if len(speedHeap) > k:
                totalSpeed -= heapq.heappop(speedHeap)

            performance = max(performance, totalSpeed * e)

        return performance % MOD
