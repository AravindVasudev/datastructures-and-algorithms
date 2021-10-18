# https://leetcode.com/problems/cousins-in-binary-tree/
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque()
        queue.append(root)
        parent = {}
        
        found = 0
        while queue:
            levelSize = len(queue)
            
            for _ in range(levelSize):
                cur = queue.popleft()
                
                if cur.val == x or cur.val == y:
                    found += 1
                
                if cur.left:
                    parent[cur.left.val] = cur
                    queue.append(cur.left)
                    
                if cur.right:
                    parent[cur.right.val] = cur
                    queue.append(cur.right)
                    
            if found == 2:
                return parent[x] != parent[y]
            elif found > 0:
                return False
            
        return False
