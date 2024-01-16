# https://leetcode.com/problems/path-sum-iv/
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree = {(num//10): (num%10) for num in nums}
        return self.totalPathSum(tree)

    def totalPathSum(self, tree: Mapping[int, int], node: int = 11, prevSum: int = 0) -> int:
        if node not in tree:
            return 0

        # Compute left and right indices.
        level, pos = node // 10, node % 10
        left = (level + 1) * 10 + pos * 2 - 1
        right = (level + 1) * 10 + pos * 2

        total = prevSum + tree[node]
        if left not in tree and right not in tree:
            return total

        return self.totalPathSum(tree, left, total) + self.totalPathSum(tree, right, total)
