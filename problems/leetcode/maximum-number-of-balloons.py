# https://leetcode.com/problems/maximum-number-of-balloons/
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charCount = defaultdict(int)
        for char in text:
            charCount[char] += 1
            
        return min(charCount['b'], charCount['a'], charCount['l'] // 2,
                   charCount['o'] // 2, charCount['n'])
