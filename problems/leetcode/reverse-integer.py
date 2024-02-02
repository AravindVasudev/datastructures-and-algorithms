# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x *= sign

        reverse = 0
        while x:
            reverse = (reverse * 10) + (x % 10)
            x //= 10

        if reverse.bit_length() > 31:
            return 0

        return reverse * sign
