# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends
class UnionFind:
    def __init__(self, N: int):
        self.parents = [i for i in range(N)]
        self.groups = N

    def find(self, x):
        parent = self.parents[x]
        while self.parents[parent] != parent:
            parent = self.parents[parent]

        return parent

    def union(self, x, y):
        parentX, parentY = self.find(x), self.find(y)

        if parentX == parentY:
            return

        self.parents[parentX] = parentY
        self.groups -= 1


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        sortedLogs = sorted(logs, key=lambda x: x[0])
        print(sortedLogs)
        uf = UnionFind(n)

        for log in sortedLogs:
            uf.union(log[1], log[2])
            if uf.groups == 1:
                return log[0]
        
        return -1
