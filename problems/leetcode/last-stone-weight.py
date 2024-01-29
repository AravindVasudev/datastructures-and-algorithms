# https://leetcode.com/problems/last-stone-weight/
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y, x = -heapq.heappop(stones), -heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0
