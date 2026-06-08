# https://leetcode.com/problems/minimum-cost-to-convert-string-i/
# Though this solution works, it has a lot of dupe computations.
# Optimal solution is Floyd Warshall.
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # 1. Construct the graph
        N = len(original)
        graph = defaultdict(list)
        for i in range(N):
            graph[original[i]].append((changed[i], cost[i]))

        # 2. Dijkstra
        @cache
        def dijkstra(start: str, end: str) -> int:
            queue = [(0, start)]
            visited = {start: 0}

            while queue:
                dist, node = heapq.heappop(queue)
                if node == end:
                    return dist

                if dist > visited[node]:
                    continue # Remove stale entries.

                for nei, cost in graph[node]:
                    nxtDist = dist + cost
                    if nei in visited and visited[nei] <= nxtDist:
                        continue

                    visited[nei] = nxtDist
                    heapq.heappush(queue, (nxtDist, nei))

            return float("inf")

        total = 0
        for i, char in enumerate(source):
            cost = dijkstra(char, target[i])
            if cost == float("inf"):
                return -1

            total += cost

        return total
