# https://leetcode.com/problems/valid-palindrome-ii/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        isPalindrome = lambda s: s == s[::-1]
        substr = lambda i: s[:i] + s[i+1:]

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return isPalindrome(substr(i)) or isPalindrome(substr(j))

            i += 1
            j -= 1

        return True
