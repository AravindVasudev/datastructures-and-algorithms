# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        def calcNext(num: int) -> int:
            newNum = 0
            while num:
                newNum += (num % 10) ** 2
                num //= 10

            return newNum

        seen = set()
        while n not in seen and n != 1:
            seen.add(n)
            n = calcNext(n)

        return n == 1

class Solution:
    def isHappy(self, n: int) -> bool:
        def calcNext(num: int) -> int:
            newNum = 0
            while num:
                newNum += (num % 10) ** 2
                num //= 10

            return newNum

        slow, fast = n, calcNext(n)
        while fast != 1 and slow != fast:
            slow = calcNext(slow)
            fast = calcNext(calcNext(fast))

        return fast == 1
