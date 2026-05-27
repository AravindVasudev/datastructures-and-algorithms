# https://leetcode.com/problems/maximum-number-of-eaten-apples/
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        N, day, eaten = len(apples), 0, 0
        heap = []

        while day < N or heap:
            if day < N and apples[day] > 0:
                heapq.heappush(heap, (day + days[day], apples[day]))

            while heap and heap[0][0] <= day:
                heapq.heappop(heap)

            if heap:
                expiration, count = heapq.heappop(heap)
                count -= 1
                eaten += 1

                if count > 0:
                    heapq.heappush(heap, (expiration, count))

            day += 1

        return eaten
