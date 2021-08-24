# https://leetcode.com/problems/word-search-ii/
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordsTrie = self.createTrie(words)
        result = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, wordsTrie, i, j, result)
                
        return result
    
    def dfs(self, board, trieNode, i, j, result):
        if trieNode.word:
            result.append(trieNode.word)
            trieNode.word = None

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        char = board[i][j]
        trieNode = trieNode.children.get(char)
        if not trieNode:
            return

        board[i][j] = '#'
        
        self.dfs(board, trieNode, i+1, j, result)
        self.dfs(board, trieNode, i-1, j, result)
        self.dfs(board, trieNode, i, j+1, result)
        self.dfs(board, trieNode, i, j-1, result)
        
        board[i][j] = char
    
    def createTrie(self, words):
        trie = TrieNode()
        
        for word in words:
            node = trie
            for w in word:
                node = node.children[w]
                
            node.word = word
            
        return trie
        
