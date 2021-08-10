# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        numComponents = 0
        visited = [False] * n

        for node in range(n):
            if visited[node]:
                continue
                
            self.dfs(graph, node, visited)
            numComponents += 1
            
        return numComponents
    
    def dfs(self, graph: List[List[int]], node: int, visited: List[bool]) -> None:
        if visited[node]:
            return
        
        visited[node] = True
        
        for connection in graph[node]:
            self.dfs(graph, connection, visited)
