# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.dfs(root, root, k)
    
    def dfs(self, root: Optional[TreeNode], cur: Optional[TreeNode], k: int) -> bool:
        if not cur:
            return False
        
        return self.search(root, cur, k - cur.val) or \
            self.dfs(root, cur.left, k) or \
            self.dfs(root, cur.right, k)
    
    def search(self, root: Optional[TreeNode], cur: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        return (root.val == k and root != cur) or \
            self.search(root.left if root.val > k else root.right, cur, k)
