# https://leetcode.com/problems/binary-tree-right-side-view/
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        rightSide = []

        while queue:
            # Peek last node.
            rightSide.append(queue[-1].val)

            levelSize = len(queue)
            for _ in range(levelSize):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return rightSide
