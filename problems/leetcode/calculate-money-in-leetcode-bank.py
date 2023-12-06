# https://leetcode.com/problems/calculate-money-in-leetcode-bank/
class Solution:
    def totalMoney(self, n: int) -> int:
        offset, saved = 0, 0

        # summation = lambda n: (n * (n + 1)) // 2
        @cache
        def summation(n):
            return (n * (n + 1)) // 2

        while n:
            days = 7 if n >= 7 else n
            saved += summation(days + offset) - summation(offset)

            offset += 1
            n -= days

        return saved
