# https://leetcode.com/problems/smallest-number-in-infinite-set/
class SmallestInfiniteSet:

    def __init__(self):
        self.nxt = 1
        self.addedSet = set()
        self.addedHeap = []

    def popSmallest(self) -> int:
        if self.addedHeap:
            self.addedSet.remove(self.addedHeap[0])
            return heapq.heappop(self.addedHeap)

        smallest = self.nxt
        self.nxt += 1
        return smallest
        

    def addBack(self, num: int) -> None:
        if num >= self.nxt or num in self.addedSet:
            return None
        
        self.addedSet.add(num)
        heapq.heappush(self.addedHeap, num)
