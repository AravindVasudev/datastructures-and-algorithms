# https://leetcode.com/problems/house-robber-iii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        include = root.val
        if root.left:
            include += self.rob(root.left.left)
            include += self.rob(root.left.right)
            
        if root.right:
            include += self.rob(root.right.left)
            include += self.rob(root.right.right)
            
        exclude = self.rob(root.left) + self.rob(root.right)
        
        return max(include, exclude)
