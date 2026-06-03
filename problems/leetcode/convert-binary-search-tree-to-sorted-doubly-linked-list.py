# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        prev, head = None, None

        def dfs(node: 'Optional[Node]') -> None:
            nonlocal prev, head
            if not node:
                return

            # In-order traverse the tree.
            dfs(node.left)
            if prev:
                prev.right = node
                node.left = prev
            else:
                head = node

            prev = node
            dfs(node.right)

        dfs(root)
        head.left, prev.right = prev, head
        return head
