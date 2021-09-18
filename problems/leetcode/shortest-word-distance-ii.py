# https://leetcode.com/problems/shortest-word-distance-ii/
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordDict = defaultdict(list)
        
        for i, word in enumerate(wordsDict):
            self.wordDict[word].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        wordList1 = self.wordDict[word1]
        wordList2 = self.wordDict[word2]

        minDistance = float('inf')
        for pos1 in wordList1:   
            for pos2 in wordList2:
                minDistance = min(minDistance, abs(pos1 - pos2))
                
        return minDistance
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
