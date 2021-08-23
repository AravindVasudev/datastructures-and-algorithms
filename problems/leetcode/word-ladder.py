# https://leetcode.com/problems/word-ladder/
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue = deque()
        visited = set()
        
        if endWord not in wordSet:
            return 0
        
        
        queue.append((beginWord, 1))
        while queue:
            word, count = queue.popleft()
            
            if word in visited:
                continue
                
            if word == endWord:
                return count
                
            visited.add(word)
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + char + word[i+1:]
                    
                    if newWord in wordSet and newWord not in visited:
                        queue.append((newWord, count + 1))
                        
        return 0

# Optimized
