# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if node is None:
                return

            counter[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        counter = defaultdict(int)
        dfs(root)

        maxFrequency = max(counter.values())
        result = []
        for node, freq in counter.items():
            if maxFrequency == freq:
                result.append(node)

        return result
