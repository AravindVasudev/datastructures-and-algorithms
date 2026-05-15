# https://leetcode.com/problems/bus-routes/
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stopToBuses = defaultdict(list)
        for i, bus in enumerate(routes):
            for stop in bus:
                stopToBuses[stop].append(i)

        queue = deque([source])
        visitedStop = set([source])
        visitedBus = set()
        level = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                stop = queue.popleft()
                if stop == target:
                    return level

                for bus in stopToBuses[stop]:
                    if bus in visitedBus:
                        continue

                    visitedBus.add(bus)
                    for nextStop in routes[bus]:
                        if nextStop not in visitedStop:
                            visitedStop.add(nextStop)
                            queue.append(nextStop)

            level += 1

        return -1
