# https://leetcode.com/problems/count-of-matches-in-tournament/
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1
        # total = 0
        # while n > 1:
        #     if n % 2:
        #         total += (n - 1) // 2
        #         n = ((n - 1) // 2) + 1
        #     else:
        #         total += n // 2
        #         n = n // 2

        # return total
