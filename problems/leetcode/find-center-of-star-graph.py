# https://leetcode.com/problems/find-center-of-star-graph/
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = set()
        for i in range(2):
            for j in range(2):
                if edges[i][j] in seen:
                    return edges[i][j]
                
                seen.add(edges[i][j])
