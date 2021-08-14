# https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            
        visited = [False] * numCourses
        order = []
        currentVisited = set()
        orderIndex = 0

        for n in range(numCourses):
            if not visited[n]:
                if not self.dfs(graph, n, visited, currentVisited, order):
                    return []
                
                currentVisited.clear()
                    
        return reversed(order)
    
    def dfs(self, graph: List[List[int]], node: int, visited: List[bool],
            currentVisited: set[int], order: List[int]) -> bool:
        if node in currentVisited:
            return False
        
        if visited[node]:
            return True

        visited[node] = True    
        currentVisited.add(node)
        for connection in graph[node]:
            if not self.dfs(graph, connection, visited, currentVisited, order):
                return False
            
        order.append(node)
        currentVisited.remove(node)
        
        return True
        
