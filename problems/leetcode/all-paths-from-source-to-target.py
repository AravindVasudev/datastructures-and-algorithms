# https://leetcode.com/problems/all-paths-from-source-to-target/
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return self.dfs(graph, [], [], 0)
    
    def dfs(self, graph: List[List[int]], paths: List[List[int]],
            currentPath: List[int], node: int):
        
        currentPath.append(node)
        if node == len(graph) - 1:
            paths.append(currentPath.copy())
            currentPath.pop()
            return paths

        for connection in graph[node]:
            self.dfs(graph, paths, currentPath, connection)
            
        currentPath.pop()
        return paths
