import heapq

class SeatManager:
    def __init__(self, n: int):
        self.nextToReserve = 1
        self.unreserved = []
        

    def reserve(self) -> int:
        if self.unreserved:
            return heapq.heappop(self.unreserved)

        nxt = self.nextToReserve
        self.nextToReserve += 1
        return nxt
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreserved, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
