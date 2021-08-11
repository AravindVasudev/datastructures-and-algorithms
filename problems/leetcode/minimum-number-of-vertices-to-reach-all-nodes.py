# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            
        visited = [False] * n
        result = [False] * n
        for node in range(n):
            if visited[node]:
                continue
                
            self.dfs(graph, node, visited, result)
            result[node] = True

        return [i for i, val in enumerate(result) if val]
    
    def dfs(self, graph: List[List[int]], node: int, visited: List[bool], result: List[bool]) -> None:
        if result[node]:
            result[node] = False

        if visited[node]:
            return
        
        visited[node] = True
        for connection in graph[node]:
            self.dfs(graph, connection, visited, result)

# Solution 2: Just return nodes with no in-degree
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        result = []
        inDegree = [False] * n
        
        for edge in edges:
            inDegree[edge[1]] = True
            
        for node, hasInDegree in enumerate(inDegree):
            if not hasInDegree:
                result.append(node)
                
        return result
