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
        wPtr1, wPtr2 = 0, 0
        while wPtr1 < len(wordList1) and wPtr2 < len(wordList2):
            minDistance = min(minDistance, abs(wordList1[wPtr1] - wordList2[wPtr2]))
            if wordList1[wPtr1] < wordList2[wPtr2]:
                wPtr1 += 1
            else:
                wPtr2 += 1
                
        return minDistance
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
