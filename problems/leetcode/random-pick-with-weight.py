# https://leetcode.com/problems/random-pick-with-weight/
class Solution:
    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i - 1]

        self.w = w
        self.total = w[-1]
        
    def pickIndex(self) -> int:
        pick = random.randint(1, self.total)
        start, end = 0, len(self.w)
        while start < end:
            mid = (start + end) // 2
            if self.w[mid] < pick:
                start = mid + 1
            else:
                end = mid

        return start
