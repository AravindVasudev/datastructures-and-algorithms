# https://leetcode.com/problems/search-in-a-binary-search-tree/
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
      if not root or val == root.val:
        return root

      nxt = root.right if val > root.val else root.left
      return self.searchBST(nxt, val)
