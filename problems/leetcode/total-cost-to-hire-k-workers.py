# https://leetcode.com/problems/total-cost-to-hire-k-workers/
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs)
        if N < k:
            return 0

        if N <= 2 * candidates:
            return sum(sorted(costs)[:k])

        considered = []
        weight = lambda c, i: (c * 100000 + i)
        reverseIndex = lambda i: N - i - 1
        for i in range(candidates):
            heapq.heappush(considered, (weight(costs[i], i), costs[i], "l"))
            ri = reverseIndex(i)
            heapq.heappush(considered, (weight(costs[ri], ri), costs[ri], "r"))

        left, right = candidates, reverseIndex(candidates)
        cost = 0
        for _ in range(k):
            _, c, d = heapq.heappop(considered)
            cost += c

            if left <= right:
                if d == "l":
                    heapq.heappush(considered,
                        (weight(costs[left], left), costs[left], d))
                    left += 1
                else:
                    heapq.heappush(considered,
                        (weight(costs[right], right), costs[right], d))
                    right -= 1

        return cost
