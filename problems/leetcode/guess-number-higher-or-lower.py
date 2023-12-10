# https://leetcode.com/problems/guess-number-higher-or-lower/
class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            mid = (l + r) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result > 0:
                l = mid + 1
            else:
                r = mid - 1

        return -1
