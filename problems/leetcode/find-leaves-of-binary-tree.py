# https://leetcode.com/problems/find-leaves-of-binary-tree/
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        while root.left or root.right:
            result.append(self.popLeaves(root, root, []))
            
        result.append([root.val])
                
        return result
    
    def popLeaves(self, root: Optional[TreeNode], parent: Optional[TreeNode],
                  result: List[int]) -> List[int]:
        if root is None:
            return None
        
        if not (root.left or root.right):
            if parent.left == root:
                parent.left = None
            else:
                parent.right = None

            return result.append(root.val)
        
        self.popLeaves(root.left, root, result)
        self.popLeaves(root.right, root, result)
        
        return result

# Efficient Solution
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node):
            if not node:
                return -1
            
            height = 1 + max(dfs(node.left), dfs(node.right))
            if height == len(result):
                result.append([])
                
            result[height].append(node.val)
            return height
        
        result = []
        dfs(root)
        
        return result
