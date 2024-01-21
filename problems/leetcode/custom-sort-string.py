# https://leetcode.com/problems/custom-sort-string/
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ordering = {c: i for i, c in enumerate(order)}
        return "".join(sorted(s, key=lambda c: ordering.get(c, 0)))
