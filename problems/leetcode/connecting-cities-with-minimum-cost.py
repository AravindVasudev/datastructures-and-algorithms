# https://leetcode.com/problems/connecting-cities-with-minimum-cost/
class UnionFind:
    def __init__(self, N: int):
        self.parents = [i for i in range(N + 1)]
        self.groups = N

    def find(self, x: int) -> int:
        parent = self.parents[x]
        while parent != self.parents[parent]:
            parent = self.parents[parent]

        return parent

    def union(self, x: int, y: int) -> bool:
        parentX, parentY = self.find(x), self.find(y)
        if parentX == parentY:
            return False

        self.parents[parentX] = parentY
        self.groups -= 1
        return True


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # Sort by cost.
        connections.sort(key=lambda x: x[2])

        uf = UnionFind(n)
        minimumCost = 0
        for x, y, cost in connections:
            if uf.union(x, y):
                minimumCost += cost
                if uf.groups == 1:
                    break

        return minimumCost if uf.groups == 1 else -1
