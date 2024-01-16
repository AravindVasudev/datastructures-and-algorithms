# https://leetcode.com/problems/find-palindrome-with-fixed-length/
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        base = 10 ** ((intLength - 1) // 2)
        result = []
        for q in queries:
            half = str(base + (q - 1))
            secondHalf = half[:-1][::-1] if intLength % 2 == 1 else half[::-1]
            palindrome = half + secondHalf
            
            result.append(
                int(palindrome) if len(palindrome) == intLength else -1)

        return result
