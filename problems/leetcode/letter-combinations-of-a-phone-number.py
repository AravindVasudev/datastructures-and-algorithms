class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToChar = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        return self.generateCombinations(digits, 0, numToChar)
    
    def generateCombinations(self, digits, cur, numToChar):
        if cur >= len(digits):
            return []
        
        nextList = self.generateCombinations(digits, cur + 1, numToChar)
        
        curList = []
        for char in numToChar[digits[cur]]:
            for item in nextList:
                curList.append(char + item)
                
        return curList if curList else numToChar[digits[cur]]
