# https://leetcode.com/problems/leaf-similar-trees/
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeafSequence(root1) == self.getLeafSequence(root2)
    
    def getLeafSequence(self, node: Optional[TreeNode]) -> str:
        if not node:
            return ""
        
        if not node.left and not node.right:
            return f".{node.val}."
        
        return self.getLeafSequence(node.left) + self.getLeafSequence(node.right)
        
