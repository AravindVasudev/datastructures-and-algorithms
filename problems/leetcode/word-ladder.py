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
# Bidriectional BFS
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return 0
        
        headVisited = {beginWord: 1}
        tailVisited = {endWord: 1}
        
        headQ = deque()
        headQ.append((beginWord, 1))
        
        tailQ = deque()
        tailQ.append((endWord, 1))
        
        while headQ and tailQ:
            found = self.bfs(headQ, headVisited, tailVisited, wordSet)
            if found > 0:
                return found
            
            found = self.bfs(tailQ, tailVisited, headVisited, wordSet)
            if found > 0:
                return found
            
        return 0
    
    def bfs(self, queue: deque[(str, int)], visited: dict[str, int], otherVisited: dict[str, int], wordSet: set[str]) -> int:
        word, level = queue.popleft()
        
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                newWord = word[:i] + char + word[i+1:]
                if newWord in wordSet:
                    if newWord in otherVisited:
                        return level + otherVisited[newWord]
                    
                    if newWord not in visited:
                        visited[newWord] = level + 1
                        queue.append((newWord, level + 1))
                        
        return 0
