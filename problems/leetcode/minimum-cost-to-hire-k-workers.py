# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(w/q, q) for q, w in zip(quality, wage)])
        
        eligibleWorkers = []
        pay, quality = float('inf'), 0

        for ratio, q in workers:
            quality += q
            heapq.heappush(eligibleWorkers, -q)

            if len(eligibleWorkers) > k:
                quality += heapq.heappop(eligibleWorkers)

            if len(eligibleWorkers) == k:
                pay = min(pay, ratio * quality)

        return pay
