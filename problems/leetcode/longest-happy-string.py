# https://leetcode.com/problems/longest-happy-string/
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, "a"))

        if b > 0:
            heapq.heappush(heap, (-b, "b"))

        if c > 0:
            heapq.heappush(heap, (-c, "c"))

        happyString = ""
        while heap:
            count, char = heapq.heappop(heap)
            if (len(happyString) > 1 and
                happyString[-2] == happyString[-1] == char):
                if not heap:
                    break # No other option, so done.

                nextCount, nextChar = heapq.heappop(heap)
                happyString += nextChar
                nextCount += 1 # count is -ve for max-heap.

                if nextCount != 0:
                    heapq.heappush(heap, (nextCount, nextChar))
            else:
                happyString += char
                count += 1 # count is -ve for max-heap.

            if count != 0:
                heapq.heappush(heap, (count, char))

        return happyString
