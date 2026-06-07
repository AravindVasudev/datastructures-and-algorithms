# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Approach 1: Dijkstra's
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for fro, to, price in flights:
            graph[fro].append((to, price))

        # best[node] = fewest steps to reach node at any cost seen so far
        best = {}
        queue = [(0, 0, src)]  # (cost, steps, node)

        while queue:
            cost, steps, node = heapq.heappop(queue)
            if node == dst:
                return cost
            if steps > k:
                continue

            if node in best and best[node] <= steps:
                continue
            best[node] = steps

            for nei, price in graph[node]:
                heapq.heappush(queue, (cost + price, steps + 1, nei))

        return -1
