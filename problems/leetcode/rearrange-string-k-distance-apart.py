# https://leetcode.com/problems/rearrange-string-k-distance-apart/
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        #1: Build a max-heap.
        counts = Counter(s)
        heap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(heap)

        reordered = ""
        waitline = deque()
        clock = 0
        while heap or waitline:
            clock += 1
            while waitline and waitline[0][0] <= clock:
                _, nxtCount, nxtChar = waitline.popleft()
                heapq.heappush(heap, (nxtCount, nxtChar))
            
            if not heap:
                return ""

            count, char = heapq.heappop(heap)
            reordered += char
            count += 1

            if count != 0:
                waitline.append((clock + k, count, char))

        return reordered
