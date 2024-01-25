# https://leetcode.com/problems/random-pick-with-weight/
"""
More Efficient Approach: Alias Method <TODO>
"""
class Solution:
    def __init__(self, w: List[int]):
        self.prefixSum = []
        self.total = 0

        for weight in w:
            self.total += weight
            self.prefixSum.append(self.total)
        

    def pickIndex(self) -> int:
        target = self.total * random.random()
        # return bisect.bisect_left(self.prefixSum, target)

        l, r = 0, len(self.prefixSum) - 1
        while l < r:
            mid = (l + r) // 2
            if target > self.prefixSum[mid]:
                l = mid + 1
            else:
                r = mid

        return l
