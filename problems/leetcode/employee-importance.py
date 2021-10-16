# https://leetcode.com/problems/employee-importance/
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:        
        return self.dfs({employee.id:employee for employee in employees}, id)

        
    def dfs(self, employees: Dict[int, 'Employee'], id: int, visited: Dict[int, int] = set()) -> int:
        if id in visited:
            return 0
        
        importance = employees[id].importance
        for subordinate in employees[id].subordinates:
            importance += self.dfs(employees, subordinate, visited)
            
        return importance
