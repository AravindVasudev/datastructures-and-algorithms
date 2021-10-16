# https://leetcode.com/problems/sentence-screen-fitting/
# Inefficient (Times out)
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        remainingRows, remainingCols = rows, cols
        fits = 0
        index = 0
        
        while remainingRows > 0:
            # Cycle if all words are fitted
            if index == len(sentence):
                index = 0
                fits += 1
                
            # Any word too large to fit in a column
            if len(sentence[index]) > cols:
                return 0
            
            if len(sentence[index]) <= remainingCols:
                remainingCols -= len(sentence[index]) + 1
                index += 1
            else:
                remainingRows -= 1
                remainingCols = cols
        
        return fits
        
# Efficient
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # Combine all words with a space in the end
        combined = " ".join(sentence) + " "
        
        start = 0
        length = len(combined)
        
        # For each row
        for _ in range(rows):
            start += cols
            
            # If can fit
            if combined[start % length] == " ":
                start += 1
            else:
                # If cannot, move back until the previous char is a space
                while start > 0 and combined[(start - 1) % length] != " ":
                    start -= 1
             
        # Number of rotations
        return start // length
