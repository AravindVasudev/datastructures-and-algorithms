# https://leetcode.com/problems/moving-average-from-data-stream/
class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val

        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()

        return self.total / len(self.queue)
