# https://leetcode.com/problems/closest-binary-search-tree-value/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        return self.dfs(root, target)[0]
    
    def dfs(self, root: Optional[TreeNode], target: float) -> (int, float):
        if root is None:
            return 0, float('inf')

        if target < root.val:
            other = self.dfs(root.left, target)
        else:
            other = self.dfs(root.right, target)
        
        rootDist = abs(target - root.val)
        return (root.val, rootDist) if rootDist < other[1] else other
