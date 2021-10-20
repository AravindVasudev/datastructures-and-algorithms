# https://leetcode.com/problems/number-of-islands-ii/
class DisjointSets:
    def __init__(self, size):
        self.parents = [-1] * size
        self.groups = 0
        
    def addParent(self, i):
        # Skip duplicates
        if self.parents[i] == -1:
            self.parents[i] = i
            self.groups += 1
        
    def find(self, x):
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]] # Path compression
            x = self.parents[x]
            
        return x

    def union(self, x, y):
        parentX, parentY = self.find(x), self.find(y)
        if parentX != parentY:
            self.groups -= 1
            self.parents[parentY] = parentX

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        getRoot = lambda x, y:  n * x + y
        
        uf = DisjointSets(m * n)
        result = []
        
        for positionX, positionY in positions:
            # Add current position to the Disjoint Sets
            root = getRoot(positionX, positionY)
            uf.addParent(root)
            
            for offsetX, offsetY in directions:
                nextX, nextY = positionX + offsetX, positionY + offsetY
                nextRoot = getRoot(nextX, nextY)
                
                if 0 <= nextX < m and 0 <= nextY < n and uf.parents[nextRoot] != -1:
                    uf.union(root, nextRoot)
                    
            result.append(uf.groups)
        
        
        return result
        
