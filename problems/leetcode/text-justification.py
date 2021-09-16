# https://leetcode.com/problems/text-justification/
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        return self.combineWords(self.groupWords(words, maxWidth), maxWidth)
    
    def groupWords(self, words: List[str], maxWidth: int) -> List[str]:
        groups = []

        curSentenceLength = 0
        curGroup = []

        for i, word in enumerate(words):
            length = len(word)                
            if (curSentenceLength + length + len(curGroup)) > maxWidth:
                groups.append((curGroup, curSentenceLength))
                curGroup = []
                curSentenceLength = 0
                
            curSentenceLength += length
            curGroup.append(word)
                
        if curGroup:
            groups.append((curGroup, curSentenceLength))
            
        return groups

    def combineWords(self, groups, maxWidth):
        sentences = []
        
        for i in range(len(groups) - 1):
            group, length = groups[i]
            wordCount = len(group)
            wordGaps = wordCount - 1
            remainingSpaces = maxWidth - length
            
            spaceAllocation = [0] * wordCount
            spaceIndex = 0
            
            if wordCount == 1:
                spaceAllocation[0] = remainingSpaces
            else:
                while remainingSpaces > 0:
                    spaceAllocation[spaceIndex] += 1
                    remainingSpaces -= 1
                    spaceIndex = (spaceIndex + 1) % wordGaps
                
            curSentence = ""
            for i in range(wordCount):
                curSentence += group[i] + " " * spaceAllocation[i]
                
            sentences.append(curSentence)
            
        lastSentence = " ".join(groups[-1][0])
        lastSentence += " " * (maxWidth - len(lastSentence))
        sentences.append(lastSentence)
            
        return sentences
