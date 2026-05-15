# https://leetcode.com/problems/shortest-way-to-form-string/
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        N = len(target)
        targetIndex, count = 0, 0

        # Repeatedly scan until target is done.
        while targetIndex < N:
            prevIndex = targetIndex

            # Do a single pass via source.
            for ch in source:
                if targetIndex < N and target[targetIndex] == ch:
                    targetIndex += 1
            
            if prevIndex == targetIndex:
                return -1 # Impossible.

            count += 1 # Add another pass

        return count
