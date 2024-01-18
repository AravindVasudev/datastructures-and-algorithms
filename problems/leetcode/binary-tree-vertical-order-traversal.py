# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        vertical = defaultdict(list)

        q = deque([(root, 0)])
        minCol, maxCol = 0, 0
        while q:
            node, level = q.popleft()
            if node:
                vertical[level].append(node.val)
                minCol = min(minCol, level)
                maxCol = max(maxCol, level)

                q.append((node.left, level - 1))
                q.append((node.right, level + 1))

        return [vertical[x] for x in range(minCol, maxCol + 1)]
