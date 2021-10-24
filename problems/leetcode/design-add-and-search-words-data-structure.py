# https://leetcode.com/problems/design-add-and-search-words-data-structure/
from dataclasses import dataclass, field

@dataclass
class TrieNode:
    children: defaultdict = field(default_factory=lambda: defaultdict(TrieNode))
    isLeaf: bool = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.children[char]
            
        cur.isLeaf = True
        

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root, 0)
    
    def dfs(self, word: str, node: TrieNode, index: int = 0) -> bool:
        if index == len(word):
            return node.isLeaf
        
        if word[index] == ".":
            for child in node.children.values():
                if self.dfs(word, child, index + 1):
                    return True
                
            return False
        
        return self.dfs(word, node.children[word[index]], index + 1) if word[index] in node.children else \
            False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
