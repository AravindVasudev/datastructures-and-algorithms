# https://leetcode.com/problems/first-unique-number/
from collections import OrderedDict, Counter

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.added = set()
        self.queue = OrderedDict()

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        return next(iter(self.queue), -1)

    def add(self, value: int) -> None:
        if value not in self.added:
            self.added.add(value)
            self.queue[value] = None
        elif value in self.queue:
            del self.queue[value]
