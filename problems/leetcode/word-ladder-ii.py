# https://leetcode.com/problems/word-ladder-ii/
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        
        if endWord not in wordList:
            return []
        
        visited = set()
        visited.add(beginWord)

        queue = deque()
        queue.append([beginWord])        
        
        result = []
        while queue:
            levelSize = len(queue)
            
            for _ in range(levelSize):
                path = queue.popleft()
                word = path[-1]
                
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + char + word[i+1:]
                        
                        if newWord in wordSet:
                            visited.add(newWord)

                            if newWord == endWord:
                                result.append(path+[newWord])
                            else:
                                queue.append(path+[newWord])
            
            for word in visited:
                if word in wordSet:
                    wordSet.remove(word)
            
            visited.clear()
                
        return result
