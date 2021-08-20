# https://leetcode.com/problems/possible-bipartition/
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])
            
        colors = [0] * (n + 1)
        for i in range(1, n + 1):
            if colors[i] == 0 and not self.dfs(graph, colors, i, 1):
                return False
            
        return True
    
    def dfs(self, graph: List[List[int]], colors: List[int], node: int, color: int) -> bool:
        if colors[node] != 0:
            return colors[node] == color
        
        colors[node] = color
        for connection in graph[node]:
            if not self.dfs(graph, colors, connection, -color):
                return False
            
        return True
