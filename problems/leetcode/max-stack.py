# https://leetcode.com/problems/max-stack/
class MaxStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        self.removed = set()
        self.id = 0
        

    def push(self, x: int) -> None:
        self.stack.append((x, self.id))
        heapq.heappush(self.heap, (-x, -self.id))
        self.id += 1
        

    def pop(self) -> int:
        self.clearInvalidated()
        self.removed.add(self.stack[-1][1])
        return self.stack.pop()[0]
        

    def top(self) -> int:
        self.clearInvalidated()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        self.clearInvalidated()
        return -self.heap[0][0]
        

    def popMax(self) -> int:
        self.clearInvalidated()
        self.removed.add(-self.heap[0][1])
        return -heapq.heappop(self.heap)[0]

    def clearInvalidated(self) -> None:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()

        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
