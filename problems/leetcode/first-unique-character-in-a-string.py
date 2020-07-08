# https://leetcode.com/problems/first-unique-character-in-a-string/
from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        charMap = OrderedDict()
        
        for i, char in enumerate(s):
            charMap[char] = -1 if char in charMap else i
        
        for char, index in charMap.items():
            if index != -1:
                return index
            
        return -1
