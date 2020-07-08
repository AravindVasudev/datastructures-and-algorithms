# https://leetcode.com/problems/first-unique-character-in-a-string/
from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        charMap = OrderedDict()
        positionMap = dict()
        
        for i, char in enumerate(s):
            if char in positionMap:
                charMap[char] += 1
                continue
                
            positionMap[char] = i
            charMap[char] = 1
        
        for char, occurence in charMap.items():
            if occurence is 1:
                return positionMap[char]
            
        return -1
