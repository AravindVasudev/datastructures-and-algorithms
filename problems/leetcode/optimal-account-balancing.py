# https://leetcode.com/problems/optimal-account-balancing/
# Inspired from: https://leetcode.com/problems/optimal-account-balancing/discuss/95355/Concise-9ms-DFS-solution-(detailed-explanation)
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debt = defaultdict(int)
        
        # Calculate everyone's debt
        for transaction in transactions:
            debt[transaction[0]] -= transaction[2]
            debt[transaction[1]] += transaction[2]
            
        return self.dfs(debt)
    
    def dfs(self, debt: Dict[int, int], index: int = 0) -> int:
        # Skip all settled debts
        while index < len(debt) and debt[index] == 0:
            index += 1
         
        # If all settled
        if index == len(debt):
            return 0
        
        transfers = float('inf')
        for i in range(index + 1, len(debt)):
            if debt[index] * debt[i] < 0:
                # Let index settle i's debt
                debt[i] += debt[index]
                
                # Find remaining number of transfers & update with min
                transfers = min(transfers, 1 + self.dfs(debt, index + 1))
                
                # Undo settling i's to try next one.
                debt[i] -= debt[index]
                
        return transfers if transfers != float('inf') else 0
