# https://leetcode.com/problems/reorganize-string/
from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapq.heapify(pq)

        result = []
        while pq:
            count, char = heapq.heappop(pq)

            if len(result) == 0 or result[-1] != char:
                result.append(char)
                count += 1
            else:
                if len(pq) == 0:
                    return ""

                secondCount, secondChar = heapq.heappop(pq)
                result.append(secondChar)
                secondCount += 1

                if secondCount != 0:
                    heapq.heappush(pq, (secondCount, secondChar))

            if count != 0:
                heapq.heappush(pq, (count, char))

        return "".join(result)
