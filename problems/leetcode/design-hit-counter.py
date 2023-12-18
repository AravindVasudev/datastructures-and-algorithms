# https://leetcode.com/problems/design-hit-counter/
class HitCounter:

    def __init__(self):
        self.hits = deque()
        self.count = 0
        

    def hit(self, timestamp: int) -> None:
        if not self.hits or self.hits[-1][0] != timestamp:
            self.hits.append((timestamp, 1))
        else:
            count = self.hits[-1][1] + 1
            self.hits.pop()
            self.hits.append((timestamp, count))

        self.count += 1
        

    def getHits(self, timestamp: int) -> int:
        while self.hits and timestamp - self.hits[0][0] >= 300:
            self.count -= self.hits[0][1]
            self.hits.popleft()

        return self.count
