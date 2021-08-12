# https://leetcode.com/problems/keys-and-rooms/
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        return self.dfs(rooms, 0, set())
    
    def dfs(self, rooms: List[List[int]], node: int, visited: set[int]) -> bool:
        if node in visited:
            return False

        visited.add(node)
        if len(visited) == len(rooms):
            return True
        
        for key in rooms[node]:
            if self.dfs(rooms, key, visited):
                return True
            
        return False
