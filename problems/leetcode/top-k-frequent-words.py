# https://leetcode.com/problems/top-k-frequent-words/
class OrderedWord:
    def __init__(self, word, count):
        self.word = word
        self.count = count
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        else:
            return self.count < other.count
        
    def __str__(self):
        return f"{self.word}:{self.count}"

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordCount = Counter(words)
        
        pqueue = []
        for word, count in wordCount.items():
            #print([str(word) for word in pqueue])
            heapq.heappush(pqueue, OrderedWord(word, count))
            
            if len(pqueue) > k:
                heapq.heappop(pqueue)

        result = []
        while pqueue:
            result.append(heapq.heappop(pqueue).word)
                
        return result[::-1]
