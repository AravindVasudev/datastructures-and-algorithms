"""
Prereq:
=======
- Binary Tree.
- Ret number of nodes where root is average of subtrees.
- Need three info from subtree: total, count, result.

Brute Force (DFS):
==================
1. If root is null: return (0, 0, 0).
2. l = dfs(root.left), r = dfs(root.right)
3. count = l[1] + r[1] + 1
4. total = l[0] + r[0] + root.val
5. avg = total / count
6. result = l.result + r.result.
7. if avg == root.val: result++
8. return (total, count result).

TC: O(N), N = number of nodes.
SC: O(N).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self._countAverageNodes(root)[2]

    def _countAverageNodes(self, root: Optional[TreeNode]) -> (int, int, int):
        if root is None:
            return (0, 0, 0)

        # Compute left & right trees.
        left = self._countAverageNodes(root.left)
        right = self._countAverageNodes(root.right)

        # Compute the result triplet.
        total = left[0] + right[0] + root.val
        count = left[1] + right[1] + 1
        avg = total // count

        # Compute result.
        result = left[2] + right[2]
        if avg == root.val:
            result += 1

        # Return result triplet.
        return (total, count, result)
