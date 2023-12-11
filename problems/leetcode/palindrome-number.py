# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == "".join(reversed(str(x)))
        if x < 0:
            return False

        def reverse(n):
            r = 0
            while n:
                r = r * 10 + (n % 10)
                n //= 10

            return r

        return x == reverse(x)
