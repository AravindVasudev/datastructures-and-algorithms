# https://leetcode.com/problems/custom-sort-string/
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ordering = {c: i for i, c in enumerate(order)}
        return "".join(sorted(s, key=lambda c: ordering.get(c, 0)))

# Custom Merge Sort
class StringSorter:
    def __init__(self, order: str):
        self.ordering = {c: i for i, c in enumerate(order)}

    def sort(self, s: str) -> str:
        if len(s) <= 1:
            return s

        mid = len(s) // 2
        left = self.sort(s[:mid])
        right = self.sort(s[mid:])

        return self._merge(left, right)

    def _merge(self, l: str, r: str) -> str:
        merged = ""
        i, j = 0, 0

        while i < len(l) and j < len(r):
            leftOrder = self.ordering.get(l[i], 0)
            rightOrder = self.ordering.get(r[j], 0)

            if leftOrder < rightOrder:
                merged += l[i]
                i += 1
            else:
                merged += r[j]
                j += 1

        if i < len(l):
            merged += l[i:]
        else:
            merged += r[j:]

        return merged

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sorter = StringSorter(order)
        return sorter.sort(s)
