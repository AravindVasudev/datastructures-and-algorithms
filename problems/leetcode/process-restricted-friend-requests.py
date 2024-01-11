# https://leetcode.com/problems/process-restricted-friend-requests/
class DisjointSets:
    def __init__(self, size: int):
        self.parents = [i for i in range(size)]

    def union(self, x: int, y: int) -> None:
        parentX, parentY = self.find(x), self.find(y)
        self.parents[parentX] = parentY

    def find(self, x: int) -> int:
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]] # Path compression
            x = self.parents[x]

        return x

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        ds = DisjointSets(n)
        result = []

        for u, v in requests:
            parentU, parentV = ds.find(u), ds.find(v)

            # Validte if any restrictions apply.
            isValid = True
            for x, y in restrictions:
                parentX, parentY = ds.find(x), ds.find(y)
                if set([parentX, parentY]) == set([parentU, parentV]):
                    isValid = False
                    break

            result.append(isValid)
            if isValid:
                ds.union(u, v)

        return result
